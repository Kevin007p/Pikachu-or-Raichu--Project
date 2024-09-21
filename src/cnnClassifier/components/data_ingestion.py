import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def check_local_file(self):
        """
        Check if the local file exists and log its size.
        """
        if os.path.exists(self.config.local_data_file):
            logger.info(f"Local file found at: {self.config.local_data_file} of size: {get_size(Path(self.config.local_data_file))}")
        else:
            logger.error(f"Local file not found at: {self.config.local_data_file}")
            raise FileNotFoundError(f"Local file not found at {self.config.local_data_file}")

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted files to: {unzip_path}")


