from django.conf.urls import include
from rest_framework import routers
from django.urls import path

from . import views
from .views import IngredientsRecetteDetail, IngredientsRecetteViewSet, RecetteViewSetByCategory, RecetteViewSetByName, RecetteViewSetByNameAndByCategory

recetteRouter = routers.DefaultRouter()
recetteRouter.register('byName', RecetteViewSetByName)
recetteRouter.register('byCategory', RecetteViewSetByCategory)
recetteRouter.register('byNameAndByCategory', RecetteViewSetByNameAndByCategory)

ingredientsRouter = routers.DefaultRouter()
ingredientsRouter.register('byRecette', IngredientsRecetteViewSet)

urlpatterns = [
    path("", views.RecetteList.as_view()),
    path("<int:pk>", views.RecetteDetail.as_view()),
    path("findRecettes/", include(recetteRouter.urls)),
    path("ingredients", views.IngredientsRecetteList.as_view()),
    path("ingredients/<int:pk>", views.IngredientsRecetteDetail.as_view()),
    path("findIngredients/", include(ingredientsRouter.urls)),
]
