from django.db import models

class CategorieRecette(models.Model) :
    name = models.CharField(max_length= 100)

    class Meta:
        ordering = ['name']

    def __str__(self) : 
        return self.name