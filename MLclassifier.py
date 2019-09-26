from . HaarClassifierFunctions import faceFinder as fd
from . HaarClassifierFunctions import haarTraining as tr
from . HaarClassifierFunctions import boundingBoxes as bd
import cv2
import os
import numpy as np


def classifierceleb(path):
    test_img = cv2.imread(path)
    print(test_img)
    face_detected, gray_img = fd.faceDetection(test_img)
    print("faces_detected: ", face_detected)

    "Training Haar Classifier"

    "This part is run only once for training"
    # faces, faceID = tr.labels_for_training_data('HaarCascadeDataset')
    # face_recognizer = tr.train_classifier(faces, faceID)
    # face_recognizer.write('trainingData.yml')
    "-----"

    "This part is run for testing"
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trainingData.yml')  # use this to load training data for subsquent ones
    " --- "
    # Dictionary of output
    name = {0: "Dalai Lama", 1: "Arsene Wenger", 2: "Genelia Dsouza",
            3: "Luiz Suarez", 4: "Sergio Aguero"}

    for face in face_detected:
        (x, y, w, h) = face
        roi_gray = gray_img[y:y + h, x:x + h]
        label, confidence = face_recognizer.predict(roi_gray)  # predicting the label
        print("Confidence:", confidence)
        print("label:", label)
        bd.draw_rect(test_img, face)
        predicted_name = name[label]
        bd.put_text(test_img, predicted_name, x, y)

    resized_img = cv2.resize(test_img, (500, 500))
    cv2.imwrite(path, resized_img)
    cv2.waitKey(0)
