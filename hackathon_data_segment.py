#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:22:43 2019

@author: eye-slash98
"""

"Dataset Information"
from os import listdir
from os.path import isfile, join

mypath = "./Dataset/Images"
file_names =  [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(str(len(file_names))+' images loaded! ')

"Dataset Splitting"

import cv2
import numpy as np
import sys
import os
import shutil

DalaiLama_count = 0
ArseneWenger_count = 0
GeneliaDsouza_count = 0
SergioAguero_count = 0
LuizSuarez_count = 0


training_size = 300
test_size = 100
training_images = []
training_labels = []
test_images = []
test_labels = []

size = 150

DalaiLama_dir_train = "./datasets/Project2/train/DalaiLama/"
ArseneWenger_dir_train = "./datasets/Project2/train/ArseneWenger/"
GeneliaDsouza_dir_train = "./datasets/Project2/train/GeneliaDsouza/"
SergioAguero_dir_train = "./datasets/Project2/train/SergioAguero/"
LuizSuarez_dir_train = "./datasets/Project2/train/LuizSuarez/"



DalaiLama_dir_val = "./datasets/Project2/val/DalaiLama/"
ArseneWenger_dir_val = "./datasets/Project2/val/ArseneWenger/"
GeneliaDsouza_dir_val = "./datasets/Project2/val/GeneliaDsouza/"
SergioAguero_dir_val = "./datasets/Project2/val/SergioAguero/"
LuizSuarez_dir_val = "./datasets/Project2/val/LuizSuarez/"


def make_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)
    
make_dir(DalaiLama_dir_train)
make_dir(ArseneWenger_dir_train)
make_dir(GeneliaDsouza_dir_train)
make_dir(SergioAguero_dir_train)
make_dir(LuizSuarez_dir_train)

make_dir(DalaiLama_dir_val)
make_dir(ArseneWenger_dir_val)
make_dir(GeneliaDsouza_dir_val)
make_dir(SergioAguero_dir_val)
make_dir(LuizSuarez_dir_val)



def getZeros(number):
    if(number > 10 and number <100):
        return "0"
    if(number < 10):
        return "00"
    else:
        return ""


def getSizedFrame(width, height):
"""Function to return an image with the size I want"""    
    s, img = self.cam.read()

    # Only process valid image frames
    if s:
            img = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
    return s, img


for i, file in enumerate(file_names):
    '''Dalai Lama'''
    if file_names[i][0] == 'D':
        DalaiLama_count += 1
        image = cv2.imread(mypath+file)
        image = cv2.resize(image, (size,size), interpolation = cv2.INTER_AREA)
        if DalaiLama_count <= training_size:
            training_images.append(image)
            training_labels.append(0)
            zeros = getZeros(DalaiLama_count)
            cv2.imwrite(DalaiLama_dir_train + 'DalaiLama' + str(zeros) + str(DalaiLama_count)+".jpg",image)
        if DalaiLama_count > training_size and DalaiLama_count <= training_size+test_size:
            test_images.append(image)
            test_labels.append(0)
            zeros = getZeros(DalaiLama_count - 300)
            cv2.imwrite(DalaiLama_dir_val + 'DalaiLama' + str(zeros) + str(DalaiLama_count - 1000) + 
                        ".jpg", image)
    
    '''Arsene Wenger'''    
    if file_names[i][0] == 'A':
        ArseneWenger_count += 1
        image = cv2.imread(mypath+file)
        image = cv2.resize(image, (size,size), interpolation = cv2.INTER_AREA)
        if ArseneWenger_count <= training_size:
            training_images.append(image)
            training_labels.append(1)
            zeros = getZeros(DalaiLama_count)
            cv2.imwrite(ArseneWenger_dir_train + 'ArseneWenger' + str(zeros) + str(ArseneWenger_count)+".jpg",image)
        if ArseneWenger_count > training_size and ArseneWenger_count <= training_size+test_size:
            test_images.append(image)
            test_labels.append(1)
            zeros = getZeros(ArseneWenger_count - 300)
            cv2.imwrite(ArseneWenger_dir_val + 'ArseneWenger' + str(zeros) + str(ArseneWenger_count - 1000) + 
                        ".jpg", image)
    
    '''Genelia Dsouza'''        
    if file_names[i][0] == 'G':
        GeneliaDsouza_count += 1
        image = cv2.imread(mypath+file)
        image = cv2.resize(image, (size,size), interpolation = cv2.INTER_AREA)
        if GeneliaDsouza_count <= training_size:
            training_images.append(image)
            training_labels.append(2)
            zeros = getZeros(GeneliaDsouza_count)
            cv2.imwrite(GeneliaDsouza_dir_train + 'GeneliaDsouza' + str(zeros) + str(GeneliaDsouza_count)+".jpg",image)
        if GeneliaDsouza_count > training_size and GeneliaDsouza_count <= training_size+test_size:
            test_images.append(image)
            test_labels.append(2)
            zeros = getZeros(GeneliaDsouza_count - 300)
            cv2.imwrite(GeneliaDsouza_dir_val + 'DalaiLama' + str(zeros) + str(GeneliaDsouza_count - 1000) + 
                        ".jpg", image)
    
    '''Sergio Aguero'''        
    if file_names[i][0] == 'S':
        SergioAguero_count += 1
        image = cv2.imread(mypath+file)
        image = cv2.resize(image, (size,size), interpolation = cv2.INTER_AREA)
        if SergioAguero_count <= training_size:
            training_images.append(image)
            training_labels.append(3)
            zeros = getZeros(SergioAguero_count)
            cv2.imwrite(SergioAguero_dir_train + 'SergioAguero' + str(zeros) + str(SergioAguero_count)+".jpg",image)
        if SergioAguero_count > training_size and SergioAguero_count <= training_size+test_size:
            test_images.append(image)
            test_labels.append(3)
            zeros = getZeros(SergioAguero_count - 300)
            cv2.imwrite(SergioAguero_dir_val + 'SergioAguero' + str(zeros) + str(SergioAguero_count - 1000) + 
                        ".jpg", image)
            
    '''LuizSuarez'''        
    if file_names[i][0] == 'L':
        LuizSuarez_count += 1
        image = cv2.imread(mypath+file)
        image = cv2.resize(image, (size,size), interpolation = cv2.INTER_AREA)
        if LuizSuarez_count <= training_size:
            training_images.append(image)
            training_labels.append(4)
            zeros = getZeros(LuizSuarez_count)
            cv2.imwrite(LuizSuarez_dir_train + 'LuizSuarez' + str(zeros) + str(LuizSuarez_count)+".jpg",image)
        if LuizSuarez_count > training_size and LuizSuarez_count <= training_size+test_size:
            test_images.append(image)
            test_labels.append(4)
            zeros = getZeros(LuizSuarez_count - 300)
            cv2.imwrite(LuizSuarez_dir_val + 'LuizSuarez' + str(zeros) + str(LuizSuarez_count - 1000) + 
                        ".jpg", image)
            
            
    if DalaiLama_count == training_size+test_size and ArseneWenger_count == training_size+test_size and GeneliaDsouza_count == training_size+test_size and SergioAguero_count == training_size+test_size and LuizSuarez_count == training_size+test_size:
        break
    
print('Training and Test data extraction complete...')


'Saving in npz format'
np.savez('hackathon_project_training_data.npz', np.array(training_images))
np.savez('hackathon_project_training_labels.npz', np.array(training_labels))
np.savez('hackathon_project_test_data.npz', np.array(test_images))
np.savez('hackathon_project_test_labels.npz', np.array(test_labels))
print('Saved successfully...')

