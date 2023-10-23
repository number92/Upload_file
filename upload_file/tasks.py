from celery import shared_task

from .models import File


@shared_task
def set_status_after_upload(obj_id):
    file = File.objects.get(id=obj_id)
    file.processed = True
    file.save()
