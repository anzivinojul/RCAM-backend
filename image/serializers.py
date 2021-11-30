from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import ImagesRecette

from versatileimagefield.serializers import VersatileImageFieldSerializer

class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
        ]
    )

    class Meta:
        model = ImagesRecette
        fields = ['pk', 'name', 'image']