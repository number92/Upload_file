from rest_framework import serializers
from upload_file.models import File


class FileSerializer(serializers.ModelSerializer):
    uploaded_at = serializers.DateTimeField('%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = File
        fields = ('file', 'uploaded_at', 'processed')
