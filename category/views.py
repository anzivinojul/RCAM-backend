from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .models import CategorieRecette
from .serializers import CategoryRecetteSerializer

class CategorieRecetteList(generics.ListAPIView) :
    queryset = CategorieRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategoryRecetteSerializer
    filter_fields = ['name']

class CategorieRecetteCreate(generics.CreateAPIView) :
    queryset = CategorieRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategoryRecetteSerializer
    filter_fields = ['name']

