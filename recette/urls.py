from django.urls import path

from . import views

urlpatterns = [
    path("", views.RecetteList.as_view()),
    path("<int:pk>", views.RecetteDetail.as_view()),
]
