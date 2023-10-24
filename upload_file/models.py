from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


class File(models.Model):
    """Модель загрузки файлов"""
    file = models.FileField(
        upload_to='files/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=settings.ALLOWED_FORMATS
                )]
        )
    uploaded_at = models.DateTimeField(
        verbose_name='Дата начала загрузки',
        auto_now_add=True,
        editable=False,
    )
    processed = models.BooleanField(
        'Состояние процесса',
        default=False
    )

    def __str__(self):
        return str(self.uploaded_at.date())
