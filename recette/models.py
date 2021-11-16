from django.db import models
from category.models import CategorieRecette

class Recette(models.Model) :
    name = models.CharField(max_length=255)
    time = models.CharField(max_length=5)
    img = models.ImageField(upload_to='recette_img', null = True)
    category = models.ForeignKey(CategorieRecette, related_name='categories', on_delete=models.SET_NULL, null = True)
    favorite = models.BooleanField()

    DifficultyType = models.TextChoices('DifficultyType', 'Facile Intermédiaire Difficile')
    difficulty = models.CharField(choices=DifficultyType.choices, max_length=20)

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