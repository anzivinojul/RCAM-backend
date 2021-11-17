from django.db.models import query
from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Recette, IngredientsRecette, PreparationRecette
from .serializers import RecetteSerializer, IngredientsRecetteSerializer, PreparationRecetteSerializer

class RecetteList(generics.ListCreateAPIView) :
    queryset = Recette.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RecetteSerializer

class RecetteDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Recette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RecetteSerializer

class RecetteViewSetByName(viewsets.ModelViewSet) :
    queryset = Recette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RecetteSerializer
    search_fields = ['name']

class RecetteViewSetByCategory(viewsets.ModelViewSet) :
    queryset = Recette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RecetteSerializer
    filter_fields = ['category__name']

class RecetteViewSetByNameAndByCategory(viewsets.ModelViewSet) :
    queryset = Recette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RecetteSerializer
    search_fields = ['name']
    filter_fields = ['category__name']

class IngredientsRecetteList(generics.ListCreateAPIView) : 
    queryset = IngredientsRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = IngredientsRecetteSerializer

class IngredientsRecetteDetail(generics.RetrieveUpdateDestroyAPIView) : 
    queryset = IngredientsRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = IngredientsRecetteSerializer

class IngredientsRecetteViewSetByRecette(viewsets.ModelViewSet) :
    queryset = IngredientsRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = IngredientsRecetteSerializer
    filterset_fields = ['recette']

class PreparationRecetteList(generics.ListCreateAPIView) :
    queryset = PreparationRecette.objects.all()
    permissions_classes = (AllowAny,)
    serializer_class = PreparationRecetteSerializer

class PreparationRecetteDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = PreparationRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PreparationRecetteSerializer

class PreparationRecetteViewSetByRecette(viewsets.ModelViewSet) : 
    queryset = PreparationRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PreparationRecetteSerializer
    filterset_fields = ['recette']
    