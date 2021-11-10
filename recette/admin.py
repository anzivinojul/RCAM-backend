from django.contrib import admin

from recette.models import Recette, IngredientsRecette, PreparationRecette

admin.site.register(Recette)
admin.site.register(IngredientsRecette)
admin.site.register(PreparationRecette)