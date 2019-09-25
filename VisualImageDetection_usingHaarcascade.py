#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:21:34 2019

@author: eye-slash98
"""

import cv2
import os
import numpy as np

def faceDetection(test_img):
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    face_haar_cascade = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
    faces = face_haar_cascade.detectMultiScale(gray_img, scaleFactor=1.32, minNeighbors=5)
    return faces, gray_img

def labels_for_training_data(directory):
    faces = []
    faceID = []
    
    for path, subdirname, filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print('Skipping System file')
                continue
            
            id = os.path.basename(path)
            img_path = os.path.join(path, filename)
            print("img_path : ",img_path)
            print('id : ',id)
            test_img = cv2.imread(img_path)
            if test_img is None:
                print("Image not loaded properly")
                continue
            faces_rect, gray_img = faceDetection(test_img)
            if len(faces_rect) != 1:
                continue
            (x,y,w,h) = faces_rect[0]
            roi_gray = gray_img[y:y+w,x:x+h]
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID


#Training our Haar Classifier with the below functions

def train_classifier(faces,faceID):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(faceID))
    return face_recognizer

#Drawing bounding boxes on detected face
def draw_rect(test_img, face):
    (x,y,w,h) = face
    cv2.rectangle(test_img, (x,y), (x+w, y+h),(255,0,0),thickness=3)
    
#Writing name of the person for detected label
def put_text(test_img, text, x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),1)
    
    
#passing a test image to the classifier
test_img = cv2.imread("./TestImages/Genelia_D'Souza.png")
face_detected, gray_img = faceDetection(test_img)
print("faces_detected: ", face_detected)


#Training Haar Classifier
#Running Once
#faces, faceID = labels_for_training_data('HaarCascadeDataset')
#face_recognizer = train_classifier(faces, faceID)
#face_recognizer.write('trainingData.yml')

#For subsequent runs
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('./HaarCascadeDataset/trainingData.yml') #use this to load training data for subsquent ones

name={0:"DalaiLama", 1: "ArseneWenger", 2:"GeneliaDsouza"} #Dict for labels

for face in face_detected:
    (x,y,w,h) = face
    roi_gray = gray_img[y:y+h, x:x+h]
    label,confidence = face_recognizer.predict(roi_gray) #predicting the label
    print("Confidence:",confidence)
    print("label:",label)
    draw_rect(test_img,face)
    predicted_name =  name[label]
    put_text(test_img, predicted_name, x, y)
    
resized_img = cv2.resize(test_img,(500,500))
cv2.imshow("",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
            

            
            
            
            
            
            
            
            
            
