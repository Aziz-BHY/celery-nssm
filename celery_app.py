from celery import Celery
import os

# Print all environment variables
print("All Environment Variables:")
for key, value in os.environ.items():
    print(f"{key} = {value}")
    
app = Celery("my_celery_app", broker="redis://localhost:6379/0")

app.conf.update(
    task_routes={"tasks.add": "default"},
    task_default_queue="default",
)
