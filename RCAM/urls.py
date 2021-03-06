"""RCAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('recettes/', include("recette.urls"), name = "recette"),
    path('category/', include("category.urls"), name = "category"),
    path('image/', include("image.urls"), name = "image"),
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls'), name="authentication"),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
