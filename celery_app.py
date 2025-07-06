from celery import Celery

app = Celery("my_celery_app", broker="redis://localhost:6379/0")

app.conf.update(
    task_routes={"tasks.add": "default"},
    task_default_queue="default",
)