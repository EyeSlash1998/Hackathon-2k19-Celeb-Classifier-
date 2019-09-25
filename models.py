from django.db import models


class image(models.Model):
    upload = models.ImageField(upload_to='uploadedimages')

    class Meta:
        db_table = "image"
