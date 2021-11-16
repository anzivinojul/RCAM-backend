from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CategorieRecette
from .serializers import CategoryRecetteSerializer

class CategorieRecetteList(generics.ListCreateAPIView) :
    queryset = CategorieRecette.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategoryRecetteSerializer

