#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:39:58 2019

@author: eye-slash98
"""

import os
os.getcwd()
collection = "./Dataset/"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("./" + filename, "./Dataset/ArseneWenger/ArseneWenger" + str(i) + ".jpg")
    
for i, filename in enumerate(os.listdir(collection)):
    os.rename("./" + filename, "./Dataset/DalaiLama/DalaiLama" + str(i) + ".jpg")

for i, filename in enumerate(os.listdir(collection)):
    os.rename("./" + filename, "./Dataset/GeneliaDsouza/GeneliaDsouza" + str(i) + ".jpg")
    
for i, filename in enumerate(os.listdir(collection)):
    os.rename("./" + filename, "./Dataset/LuizSuarez/LuizSuarez" + str(i) + ".jpg")
    
for i, filename in enumerate(os.listdir(collection)):
    os.rename("./" + filename, "./Dataset/SergioAguero/SergioAguero" + str(i) + ".jpg")

