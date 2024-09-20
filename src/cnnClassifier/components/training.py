from cnnClassifier.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        # Load the base model from the given path
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

        # Recompile the model with a new optimizer (this ensures no optimizer issues)
        self.model.compile(optimizer=tf.keras.optimizers.Adam(), 
                           loss='categorical_crossentropy', 
                           metrics=['accuracy'])

    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],  # Ensure this matches the model input
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        # Validation data generator
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        # Training data generator with augmentation if enabled
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        # Training data generator
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        # Save the trained model to the given path
        model.save(path)

    def train(self, callback_list: list):
        # Define steps per epoch for training and validation
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size


        # Early stopping callback: stop training when no improvement is seen in validation loss
        early_stopping = tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',  # Track validation loss to decide when to stop
            patience=3,  # Stop training if no improvement for 3 epochs
            restore_best_weights=True  # Restore model to best epoch's weights
        )

        # Add EarlyStopping to the callback list
        callback_list.append(early_stopping)

        # Train the model using the generators and callbacks
        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        # Save the trained model
        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )


