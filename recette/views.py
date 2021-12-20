from django.db.models import query
from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Recette, IngredientsRecette, PreparationRecette
from .serializers import RecetteDetailSerializer, RecetteSerializer, IngredientsRecetteSerializer, PreparationRecetteSerializer

class RecetteList(generics.ListCreateAPIView) :
    queryset = Recette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RecetteDetailSerializer
    search_fields = ['name']
    filter_fields = ['category__name']

class RecetteDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Recette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RecetteDetailSerializer

class RecetteCreate(generics.CreateAPIView) :
    queryset = Recette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RecetteSerializer

class RecetteUpdate(generics.UpdateAPIView) :
    queryset = Recette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RecetteSerializer

class RecetteDelete(generics.DestroyAPIView) :
    queryset = Recette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RecetteSerializer

class IngredientsRecetteList(generics.ListCreateAPIView) : 
    queryset = IngredientsRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = IngredientsRecetteSerializer
    filterset_fields = ['recette']

class IngredientsRecetteDetail(generics.RetrieveUpdateDestroyAPIView) : 
    queryset = IngredientsRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = IngredientsRecetteSerializer

class PreparationRecetteList(generics.ListCreateAPIView) :
    queryset = PreparationRecette.objects.all()
    permissions_classes = (AllowAny,)
    serializer_class = PreparationRecetteSerializer
    filterset_fields = ['recette']

class PreparationRecetteDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = PreparationRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PreparationRecetteSerializer

    