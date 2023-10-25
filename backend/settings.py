import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-f)!#lv8=d%)s-r@(ds-2jm4k^-t+6ic-gl8ji8g^zetb^b0kf='

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'testserver',]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'upload_file.apps.UploadFileConfig',
    'api.apps.ApiConfig',
    'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

redis_host = os.environ.get('REDIS_HOST', 'localhost')
# Channel layer definitions
# http://channels.readthedocs.org/en/latest/deploying.html#setting-up-a-channel-backend

# Celery
REDIS_HOST = 'redis'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
# CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True


ALLOWED_FORMATS = [
    # Image
    'bmp', 'gif', 'ico', 'jp2', 'jpeg', 'jpg', 'png', 'psd', 'tiff', 'webp',
    # Video
    '3g2', '3gp', 'asf', 'avi', 'flv', 'm4v', 'mkv', 'mov', 'mp4', 'mpg',
    'ogv', 'swf', 'vob', 'webm', 'wmv',
    # Document
    'doc', 'docx', 'epub', 'key', 'numbers', 'odp', 'ods', 'odt', 'pages',
    'pdf', 'pps', 'ppt', 'pptx', 'rtf', 'xls', 'xlsx', 'xml',
    # Archive
    '7z', 'dmg', 'gz', 'iso', 'rar', 'tar.z', 'zip',
]
