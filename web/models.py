from django.db import models
from versatileimagefield.fields import VersatileImageField

# Create your models here.

class Gallery(models.Model):
    gallery_image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    caption = models.CharField(max_length=100)

    def __str__(self):
        return str(self.gallery_image)