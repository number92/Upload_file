from django.urls import path, include
from api.views import UploadFileView, FileListView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'upload', UploadFileView, basename='upload')
router.register(r'files', FileListView, basename='files')


urlpatterns = [
    path('', include(router.urls)),
]
