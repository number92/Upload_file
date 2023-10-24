import tempfile
from datetime import date, datetime
from http import HTTPStatus

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings

from .models import File
from .tasks import set_status_after_upload

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


class FileUploadingTest(TestCase):
    def test_file_uploading(self):
        file = File.objects.create(file='testname.txt', processed=True)
        set_status_after_upload(file.id)
        file.refresh_from_db()
        self.assertTrue(file.processed)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class ApiPagesURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )
    """Проверка статус кода и методов запроса энпоинтов"""
    def setUp(self):
        self.guest_client = Client()

    def test_files_url(self):
        """Проверка статуса эндпоинта"""
        response = self.guest_client.get('/api/files/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_upload_url(self):
        """Проверка отправки файла /Запускать в контейнере с redis"""
        uploaded_test = SimpleUploadedFile(
            name='test_small.gif',
            content=ApiPagesURLTests.small_gif,
            content_type='image/gif'
        )
        response = self.guest_client.post('/api/upload/',
                                          data={'file': uploaded_test})
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_negative_method_request(self):
        """"проверка метод get не доступен"""
        response_get = self.guest_client.get('/api/upload/')
        self.assertEqual(response_get.status_code,
                         HTTPStatus.METHOD_NOT_ALLOWED)


class FileViewTests(TestCase):
    """Проверка: обьект не создается без файла"""
    def test_file_not_created(self):
        File.objects.create(
            uploaded_at=datetime.now(),
            processed=True
        )
        files = File.objects.all()
        self.assertTrue(files.count(), 0)


class FileModelTests(TestCase):
    """Проверка метода str модели"""
    def test_str(self):
        file = File.objects.create(file='test.txt',
                                   uploaded_at=datetime.now(),
                                   processed=True)
        self.assertEqual(str(file), str(date.today()))

    def test_upload_to(self):
        file = File.objects.create(file='test.txt',
                                   uploaded_at=datetime.now(),
                                   processed=True)
        self.assertEqual(file.file.field.upload_to, 'files/')

    def test_processed(self):
        file = File.objects.create(file='test.txt',
                                   uploaded_at=datetime.now(),
                                   processed=False)
        self.assertFalse(file.processed)
