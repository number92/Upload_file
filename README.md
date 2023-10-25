[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=flat-square&logo=redis&logoColor=white)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

# Upload_file
API, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.
1. 'api/upload/' - эндпоинт для загрузки файла
2. 'api/files/' - эндпоинт для просмотра списка загруженных файлов


## Как запустить
* Запустить контейнеры
```
docker compose up -d
```
* Выполнить миграции

```
docker compose exec backend python manage.py migrate
```
* Запутить воркер celery
```
docker compose exec backend celery -A backend worker -l info
```
проверить по адресу http://127.0.0.1:8000/api/

## Стек
•	Python 3.9.10
•	Django==4.2.6
•	djangorestframework==3.14.0
•	celery==5.3.4
•	redis==4.6.0
