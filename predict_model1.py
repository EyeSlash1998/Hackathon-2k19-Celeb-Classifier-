#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:34:49 2019

@author: eye-slash98
"""
import numpy as np
import cv2
from tensorflow.keras.models import load_model


model = load_model('./model/CelebModel.h5')

img_path = "./TestImages/GeneliaDsouza32.jpg"
	
img_array = cv2.imread(img_path)

new_path=[]
new_path = cv2.resize(img_array, (150,150))

    #Convert to array and reshape
to_predict_data = np.array(new_path).reshape(1,150,150,3)
    #Normalize
to_predict_data = to_predict_data/255

predicted_data = model.predict(to_predict_data)
    
output_label = ['Dalai Lama','Arsene Wenger','Genelia Dsouza', 'Luiz Suarez', 'Sergio Aguero']

print(predicted_data)
predicted_class = np.argmax(predicted_data)
print('Class index : ',predicted_class)
print('Prediction : Image is ',output_label[predicted_class])
	
	
