# images/serializers.py
from rest_framework import serializers
from .models import Image

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('original', 'project_id')
