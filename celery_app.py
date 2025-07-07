from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env into os.environ

# Print all environment variables
for key, value in os.environ.items():
    print(f"{key}={value}")

app = Celery("my_celery_app", broker="redis://localhost:6379/0")

app.conf.update(
    task_routes={"tasks.add": "default"},
    task_default_queue="default",
)
