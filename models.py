from django.db import models


# MODEL CREATIONS

class ImageUpload(models.Model):
    document = models.ImageField(upload_to='images')
