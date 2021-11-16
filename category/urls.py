from django.urls import path

from . import views

urlpatterns = [
    path("", views.CategorieRecetteList.as_view()),
]
