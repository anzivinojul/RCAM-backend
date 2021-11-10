from django.db import models

class Recette(models.Model) :
    name = models.CharField(max_length=255)
    time = models.CharField(max_length=5)
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