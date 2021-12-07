from rest_framework import serializers
from .models import CategorieRecette

class CategoryRecetteSerializer(serializers.ModelSerializer) :
    class Meta :
        model = CategorieRecette
        fields = '__all__'