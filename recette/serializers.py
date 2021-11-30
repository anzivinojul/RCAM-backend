from rest_framework import serializers
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin
from versatileimagefield.serializers import VersatileImageFieldSerializer

from category.serializers import CategoryRecetteSerializer
from image.serializers import ImageSerializer
from .models import IngredientsRecette, PreparationRecette, Recette

class RecetteSerializer(SerializerExtensionsMixin, serializers.ModelSerializer) :
    img = ImageSerializer(read_only = True)
    category = CategoryRecetteSerializer()

    class Meta : 
        model = Recette
        fields = ['id', 'name', 'time_preparation', 'time_cooking', 'img', 'category', 'favorite', 'difficulty']

class IngredientsRecetteSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = IngredientsRecette
        fields = '__all__'

class PreparationRecetteSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = PreparationRecette
        fields = '__all__'