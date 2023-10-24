from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import FileListView, UploadFileView

router = DefaultRouter()
router.register(r'upload', UploadFileView, basename='upload')
router.register(r'files', FileListView, basename='files')


urlpatterns = [
    path('', include(router.urls)),
]
