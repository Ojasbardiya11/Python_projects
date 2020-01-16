#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#@author Ojas Bardiya


import random

#function 1 - modifies list depending on the comparison between the index and the element 

def largerIndex(c):
    for i in range(len(c)):
        if (c[i] < i):
            c[i] = -1
        elif (c[i] == i):
            c[i] = 0
        elif (c[i] > i):
            c[i] = 1
            
    return c

l1 = [1, 2, 0, 4, 2, 1, 40, -5]
l2 = [0, 3, 2, 1, 32, 3, 4, 0]

#function 2 - returns all integers that are perfect squares up until the specified limit

def squareUpTo(n):
    squarelist = []
    for i in range(n):
        a = i*i
        if (a <= n):
            squarelist.append(a)
        else:
            break
    return squarelist

#function 3 - has a 1/3 probability of returning true and 2/3 probability of returning false
#achieves this by using fair coins to simulate a biased coin
    
def flip1in3():
    faircointoss = ['HH', 'HT', 'TH', 'TT'] #the elements of this list consists of all of the possible outcomes of a double coin flip
    flip = random.randint(0, 3)             # generates a random integer between 0 and 3
    while flip == 0:                        # this disregards the case of 'HH' to simulate only 3 possible outcomes for the double coin flip
        flip = random.randint(0, 3)
    element = faircointoss[flip]
    if element == 'HT' or element == 'TH':       #2 outcomes out of 3 lead to False
        return False
    elif element == 'TT':                        #only 1 outcome out of three leads to True     
        return True
    
    
#function 4 - outputs all elements of a list that appear twice
        
def duplicates(c):
    c.sort()                                #sorts the list in ascending order
    new_list = []                           #list that will contain duplicate values
    for i in range(len(c) - 1):
        if c[i] == c[i+1]:
            new_list.append(c[i])           #since no element is repeated more than once, duplicates will be next to each other
    return new_list
            



            
        
   
            



            
    