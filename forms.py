from django import forms
from .models import ImageUpload


# Image Upload Form - Website

class ImageUploadForm(forms.ModelForm):
    # image = forms.ImageField()

    class Meta:
        model = ImageUpload
        fields = "__all__"
