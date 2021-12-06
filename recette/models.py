from enum import unique
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.deletion import CASCADE
from category.models import CategorieRecette
from image.models import ImagesRecette

class Recette(models.Model) :
    name = models.CharField(max_length=255)
    time_preparation = models.CharField(max_length=5, null = True)
    time_cooking = models.CharField(max_length=5, null = True)
    people_number = models.CharField(max_length=2, default='1')
    img = models.ForeignKey(ImagesRecette, related_name='images', on_delete=models.SET_DEFAULT, default=1)
    category = models.ForeignKey(CategorieRecette, related_name='categories', on_delete=models.SET_NULL, null = True)
    favorite = models.BooleanField()

    DifficultyType = models.TextChoices('DifficultyType', 'Facile Intermédiaire Difficile')
    difficulty = models.CharField(choices=DifficultyType.choices, max_length=20)

    class Meta: 
        ordering = ['name']

    def __str__(self) :
        return self.name

class IngredientsRecette(models.Model) :

    name = models.CharField(max_length=255)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)

    def __str__(self) :
        return self.recette.name + ' - ' + self.name

class PreparationRecette(models.Model) :

    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)

    preparation = models.JSONField()

    def __str__(self) :
        return self.recette.name
