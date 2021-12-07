from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework import routers

from . import views

urlpatterns = [
    path("", views.ImageViewSet.as_view({'get': 'list'})),
    path("", views.ImageViewSet.as_view({'post': 'list'})),
    path("", views.ImageViewSet.as_view({'put': 'list'})),
    path("", views.ImageViewSet.as_view({'delete': 'list'})),
]


