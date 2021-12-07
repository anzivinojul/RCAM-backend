from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import ImagesRecette

from versatileimagefield.serializers import VersatileImageFieldSerializer

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesRecette
        fields = '__all__'