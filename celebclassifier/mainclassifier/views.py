from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from . MLclassifier import classifierceleb


# DEFAULT ROUTE
def firstpage(request):
    return render(request, 'firstpage.html', {})


# FACE UPLOAD ROUTE
def dface(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save()
            post.save()
            # settings.MEDIA_ROOT_URL +
            imageURL = settings.MEDIA_URL + form.instance.document.name
            classifierceleb(imageURL)

            return render(request, 'uploadface.html', {'form': form, 'post': post})
    else:
        form = ImageUploadForm()
    return render(request, 'uploadface.html', {'form': form})
