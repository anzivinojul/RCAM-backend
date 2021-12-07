from django.urls import path
from .views import CategorieRecetteCreate, CategorieRecetteList

urlpatterns = [
    path("", CategorieRecetteList.as_view()),
    path("add", CategorieRecetteCreate.as_view()),
]
