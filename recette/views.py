from django.db.models import query
from django.shortcuts import render

from rest_framework import generics, viewsets
from .models import Recette, IngredientsRecette, PreparationRecette
from .serializers import RecetteSerializer, IngredientsRecetteSerializer, PreparationRecetteSerializer

class RecetteList(generics.ListCreateAPIView) :
    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer

class RecetteDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer

class IngredientsRecetteList(generics.ListCreateAPIView) : 
    queryset = IngredientsRecette.objects.all()
    serializer_class = IngredientsRecetteSerializer

class IngredientsRecetteDetail(generics.RetrieveUpdateDestroyAPIView) : 
    queryset = IngredientsRecette.objects.all()
    serializer_class = IngredientsRecetteSerializer

class IngredientsRecetteDetailByRecette(viewsets.ModelViewSet) :
    queryset = IngredientsRecette.objects.all()
    serializer_class = IngredientsRecetteSerializer