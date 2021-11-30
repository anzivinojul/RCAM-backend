from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework import routers

from . import views

imageRouter = routers.DefaultRouter()
imageRouter.register('', views.ImageViewSet)

urlpatterns = [
    path("", include(imageRouter.urls)),
]


