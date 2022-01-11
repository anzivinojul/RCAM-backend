from django.db import models

# Create your models here.
class ImagesRecette(models.Model) :

    name = models.CharField(max_length=255)
    image = models.ImageField(blank = False, default=1)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs): 
        self.image.delete()
        super().delete(*args, **kwargs)

