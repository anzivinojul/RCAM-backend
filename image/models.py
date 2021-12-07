from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField

# Create your models here.
class ImagesRecette(models.Model) :

    name = models.CharField(max_length=255)
    image = models.ImageField(blank = False, default=9)

    def __str__(self):
        return self.name

