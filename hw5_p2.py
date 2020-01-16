#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:24:12 2019

@author: ojasbardiya
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as matimg

img_1 = matimg.imread('g.jpg')
img_2 = matimg.imread('h.jpg')

#convert both into dtype int64
intimg_1 = img_1.astype(np.int64)
intimg_2 = img_2.astype(np.int64)


diff_img = abs(intimg_1 - intimg_2)
img_i = diff_img.astype(np.uint8)

plt.imsave('i.jpg', img_i)

#Testing
#img = plt.imread('i.jpg')
#plt.imshow(img)









