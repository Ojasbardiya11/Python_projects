#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:17:43 2019

@author: ojasbardiya
"""

import matplotlib.pyplot as plt
import matplotlib.image as matimg
import numpy as np
import math 
        
def matrix_multi(M1, M2, return_total = True):
    
    #check dimension 
    if (M1.shape != M2.shape):
        print("dimension not match")
    #    return M1, M2
    
    new_matrix = np.zeros(M1.shape)
    
    for i in range(M1.shape[0]):
        for j in range(M1.shape[1]):
            new_matrix[i][j] = M1[i][j] * M2[i][j]
    if return_total == False:
        return new_matrix
    return np.sum(new_matrix)

"""
m_input: image
option: horizontal, vertical or both
"""
def detect_edge(m_input, option):
    
    #3 by 3 operating matrix
    horizontal = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    vertical = np.array([[1,2,1], [0,0,0], [-1,-2,-1]])  
    
    m_input = np.array(m_input)
    edge = m_input
    m = matimg.imread(m_input)
    m = m.astype(np.float64)
    row_len = m_input.shape[0]
    col_len = m_input.shape[1]
       
    for i in range(0, row_len - 2):
        for j in range(0, col_len - 2):
            
            submatrix = m[i: (i + 3), :]
            submatrix = submatrix[:, j:(j+3)]
            Gx = matrix_multi(submatrix, horizontal)
            Gy = matrix_multi(submatrix, vertical)
            
            if option == "horizontal":
                edge[i][j] = Gx
            elif option == "vertical":
                edge[i][j] = Gy
            elif option == "both":
                edge[i][j] = np.sqrt(Gx**2 + Gy**2)
                
    plt.imshow(edge)
    return edge
        
img = matimg.imread('kitty-cat.jpg')
#plt.imshow(img)
detect_edge('kitty-cat.jpg', 'horizontal')

        

        
    
                 
                 
                 
                 
                 
                 
        
                  
                 
                 
                 

        
    
    
    
                 
             
             
             
             
     
     
  
             
             
     
     
   
     
     
     
     
        
    