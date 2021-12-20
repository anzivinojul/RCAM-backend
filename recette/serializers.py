from rest_framework import serializers
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin
from versatileimagefield.serializers import VersatileImageFieldSerializer

from category.serializers import CategoryRecetteSerializer
from image.serializers import ImageSerializer
from .models import IngredientsRecette, PreparationRecette, Recette

class RecetteDetailSerializer(SerializerExtensionsMixin, serializers.ModelSerializer) :
    img = ImageSerializer(read_only = True)
    category = CategoryRecetteSerializer(read_only = True)

    class Meta : 
        model = Recette
        fields = '__all__'

class RecetteSerializer(SerializerExtensionsMixin, serializers.ModelSerializer) :

    class Meta : 
        model = Recette
        fields = '__all__'

class IngredientsRecetteSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = IngredientsRecette
        fields = '__all__'

class PreparationRecetteSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = PreparationRecette
        fields = '__all__'