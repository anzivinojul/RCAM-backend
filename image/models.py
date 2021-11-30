from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField

# Create your models here.
class ImagesRecette(models.Model) :

    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='recette_img/',
        ppoi_field='image_ppoi', 
        null = True,
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name

