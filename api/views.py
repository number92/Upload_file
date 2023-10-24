from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from upload_file.models import File
from upload_file.tasks import set_status_after_upload
from .serializers import FileSerializer, FileListSerializer


class UploadFileView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (FormParser, MultiPartParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            file = serializer.save()
            print(file)
            set_status_after_upload.delay(file.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileListSerializer
    parser_classes = (FormParser, MultiPartParser)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
