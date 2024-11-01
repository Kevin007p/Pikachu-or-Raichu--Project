# Pikachu-or-Raichu--Project

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/4765f4b2-ede9-41ac-bab9-d68fad14ac2a/da9jbkx-971a3dd6-fded-4bf0-ac58-4deafeebb5fb.png/v1/fill/w_1192,h_670,q_70,strp/raichu_and_pikachu_render_by_dakotaatokad_da9jbkx-pre.jpg" alt="Pikachu and Raichu" width="500">


## How to Run?

### Steps:
1. Clone the repository:

   ```
   https://github.com/Kevin007p/Pikachu-or-Raichu--Project
   ```

2. Create a conda environment after opening the repository

   ```
   conda create -n cnnpokemon python=3.8 -y
   ```

   ```
   conda activate cnnpokemon
   ```

3. install the requirements

   ```
   pip install -r requirements.txt
   ```

   ```
   # Now run
   python app.py
   ```

4. Upload a picture and click predict :)

   <img width="1154" alt="image" src="https://github.com/user-attachments/assets/0fda5e30-14a6-439a-a080-3fa1f297e007">


> **Note:**
> - Used **DVC** for data version control.
> - Implemented **AWS CI/CD deployment** using **GitHub Actions**.
> - Managed resources in the **AWS Console** with **IAM** for access control.
> - Built a **Docker image** of the source code and pushed it to **ECR**.
> - Pulled the Docker image from **ECR** to **EC2** and launched the container.
> - Currently turned off the deployment to avoid incurring costs.

