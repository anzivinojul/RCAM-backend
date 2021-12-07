from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework import routers

from . import views

urlpatterns = [
    path("", views.ImageList.as_view()),
    path("add", views.ImageCreateView.as_view())
]


