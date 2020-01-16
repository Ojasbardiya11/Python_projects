#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:43:46 2019

@author: ojasbardiya
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as matimg

img_1=matimg.imread('a.jpg')
img_2=matimg.imread('b.jpg')
x = img_2.shape
y = img_1.shape

#find coordinates of center
min_vertical = (y[0] - x[0])/2
max_vertical = (y[0] + x[0])/2
min_horizontal = (y[1] - x[1])/2
max_horizontal = (y[1] + x[1])/2

img_c = img_1.copy()
img_c[min_vertical:max_vertical, min_horizontal:max_horizontal] = img_2 #attach img_2 to the center of img_1
plt.imsave('c.jpg', img_c) #save the image


#Testing
#img = matimg.imread('c.jpg')
#plt.imshow(img)










