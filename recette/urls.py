from django.conf.urls import include
from rest_framework import routers
from django.urls import path

from . import views

urlpatterns = [
    path("", views.RecetteList.as_view()),
    path("<int:pk>", views.RecetteDetail.as_view()),
    path("add", views.RecetteCreate.as_view()),
    path("update/<int:pk>", views.RecetteUpdate.as_view()),
    path("delete/<int:pk>", views.RecetteDelete.as_view()),
    path("ingredients", views.IngredientsRecetteList.as_view()),
    path("ingredients/<int:pk>", views.IngredientsRecetteDetail.as_view()),
    path("preparations", views.PreparationRecetteList.as_view()),
    path("preparations/<int:pk>", views.PreparationRecetteDetail.as_view()),
]