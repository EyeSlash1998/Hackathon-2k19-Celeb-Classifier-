# from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import image
from .form import imageForm

# Classifier Libraries by ROHAN
# import os
# import numpy as np
# import cv2
# from imagewebapp import settings
# from tensorflow.keras.models import load_model
#
# loaded_model = load_model('./CelebModel.model')


# MACHINE LEARNING MODEL

# MACHINE LEARNING MODEL ENDS

# ROUTES


def upload_img(request):
    if request.method == 'POST':
        form = image(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('predict')

    else:
        form = image()

    return render(request, "index.html", {'form': form})

# def predict(request):
#     img_path = 'C:/Users/sinan/Desktop/HACKATHON/imagewebapp/classifier/media/uploadedimages/'
#     print(img_path)
#     img_array = cv2.imread(img_path)
#     new_path = []
#     new_path = cv2.resize(img_array, (150, 150))
#
#     to_predict_data = np.array(new_path).reshape(1, 150, 150, 3)
#     to_predict_data = to_predict_data / 255
#
#     preds = loaded_model.predict(to_predict_data)
#
#     classes = ['Dalai Lama', 'Arsene Wenger',
#                'Genelia Dsouza', 'Luiz Suarez', 'Sergio Aguero']
#
#     image_name = classes[np.argmax(to_predict_data)]
#
#     context = {'image_name': image_name}
#     print(context)
#
#     return render(request, 'index.html', context)

def predict(request):
    print("Request Handling")
    pic = request.FILES['image']
    upload = image(upload = pic)
    upload.save()


    return render(request, "index.html")
