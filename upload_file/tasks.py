from backend.celery import app

from .models import File


@app.task
def set_status_after_upload(obj_id):
    File.objects.filter(id=obj_id).update(processed=True)
