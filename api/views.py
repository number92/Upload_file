from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from upload_file.models import File
from .serializers import FileSerializer


class UploadFileView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = FileSerializer
    parser_classes = (FormParser, MultiPartParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FileSerializer
    parser_classes = (FormParser, MultiPartParser)
    queryset = File.objects.all()
