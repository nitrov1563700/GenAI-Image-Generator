import mlflow

mlflow.set_experiments("GenAI-Image-Generator")

def log_run(prompt, image_path):
    with mlflow.start_run():
        mlflow.log_param("prompt", prompt)
        mlflow.log_artifact(image_path)