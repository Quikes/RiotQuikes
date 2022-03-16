from .models import Image, Thumbnail
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'
        read_only_fields = ('name',)