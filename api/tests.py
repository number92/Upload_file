from django.test import Client, TestCase


class FileViewTest(TestCase):
    def setUp(self) -> None:
        self.guest_client = Client()

    def test_response_is_list(self):
        """Проверка: ответ возвращает список"""
        response = self.guest_client.get('/api/files/')
        self.assertListEqual(response.data, [])
