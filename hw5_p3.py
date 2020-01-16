#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:23:50 2019

@author: ojasbardiya
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as matimg

img_1 = matimg.imread('e.jpg')
img_2 = matimg.imread('d.jpg')

img_copy1 = img_1.copy()
img_copy2 = img_2.copy()

#replace the green background with black
mask = np.logical_and(img_copy1[:,:,0] < 50, img_copy1[:,:,1] >200, img_copy1[:,:,2] < 50)
img_copy1[mask] = 0

#isolate the minion from the image
for i in range(img_1.shape[0]):
    for j in range(img_1.shape[1]):  #loop through the entire image via each pixel
        if np.linalg.norm(np.subtract(img_copy1[i, j], [0, 0, 0])) != 0: #if the pixel is not black, then attach it to the other image
            img_copy2[585 + i, 245 + j] = img_copy1[i, j] #coordinates on where to put the minion approximated

plt.imsave('f.jpg', img_copy2) 

#Testing
#img = matimg.imread('f.jpg')
#plt.imshow(img)  





            