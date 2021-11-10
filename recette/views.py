from django.db.models import query
from django.shortcuts import render

from rest_framework import generics
from .models import Recette, IngredientsRecette, PreparationRecette
from .serializers import RecetteSerializer, IngredientsRecetteSerializer, PreparationRecetteSerializer

class RecetteList(generics.ListCreateAPIView) :
    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer

class RecetteDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer