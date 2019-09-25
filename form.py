from django import forms
from classifier.models import image


class imageForm(forms.ModelForm):
    class Meta:
        model = image
        fields = "__all__"
