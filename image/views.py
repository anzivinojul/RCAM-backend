from django.db.models import query
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import ImagesRecette
from .serializers import ImageSerializer
from rest_flex_fields.views import FlexFieldsModelViewSet
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import generics, status

class ImageList(generics.ListAPIView):

    queryset = ImagesRecette.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)
    filter_fields = ['name']

class ImageDelete(generics.DestroyAPIView):
    queryset = ImagesRecette.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)

class ImageCreateView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      img_serializer = ImageSerializer(data=request.data)

      if img_serializer.is_valid():
          img_serializer.save()
          return Response(img_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(img_serializer.errors, status=status.HTTP_400_BAD_REQUEST)