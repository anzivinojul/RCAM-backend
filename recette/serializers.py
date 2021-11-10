from rest_framework import serializers
from .models import IngredientsRecette, PreparationRecette, Recette

class RecetteSerializer(serializers.ModelSerializer) :
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