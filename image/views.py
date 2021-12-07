from .models import ImagesRecette
from .serializers import ImageSerializer
from rest_flex_fields.views import FlexFieldsModelViewSet

class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = ImagesRecette.objects.all()
    filter_fields = ['name']