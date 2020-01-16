#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:48:11 2019

@author: ojasbardiya
"""

import re
import urllib2
from happiness_dictionary import happiness_dictionary as hp

def mytype(v):
    
    s = str(v)
    
    if re.search(r'^\[.*\]$', s):        #list is checked first
        return "list"
    
    if re.search(r'[a-zA-Z]+', s):       #string is checked next so that if digits are present in a string it is read as string and not int
        return "string"
    
    if re.search(r'\d*\.\d+', s):        #float is checked before int
        return "float"
    
    if re.search(r'[0-9]+', s):         #int is checked last
        return "int"
 

#a = ['floss', 34, 'lezzgo', 3.2]
#z = mytype(a)
#print z
    

def findpdfs(L):
    list_of_pdfs = []
    for i in L:
        if re.search(r'^(\w+)\.pdf$', i):       #search for all files ending with a pdf extension and group out the name of the file
            list_of_pdfs.append(re.search(r'^(\w+)\.pdf$', i).group(1))  #append the name of the file to the list
    return list_of_pdfs   


#L = ["IMG2309.jpg", "lecture1.pdf", "homework.pdf", "homework2.pdf", "resume.pdf", "test.py", "Kalah.cpp", "essay1.docx"]
#x = findpdfs(L)
#print x
    

def findemail(url):
    page = urllib2.urlopen(url).read()
    email_addresses = []  #create empty list to hold emails
    l1 = re.findall(r'\w+@\w+\.\w+\.\w+', page)
    for i in l1:
        email_addresses.append(i)
    l2 = re.findall(r'\w+ AT \w+ DOT \w+ DOT \w+', page)
    for i in l2:
        email_addresses.append(re.sub(r'(\w+) AT (\w+) DOT (\w+) DOT (\w+)',r'\1@\2.\3.\4', i ))  #change the masked form to regular and add it to the list
    l3 = re.findall(r'\w+ at \w+ dot \w+ dot \w+', page)
    for i in l3:
        email_addresses.append(re.sub(r'(\w+) at (\w+) dot (\w+) dot (\w+)',r'\1@\2.\3.\4', i ))  #change the masked form to regular and add it to the list
    l4 = re.findall(r'\w+\[AT\]\w+\[DOT\]\w+', page)
    for i  in l4:
        email_addresses.append(re.sub(r'(\w+)\[AT\](\w+)\[DOT\](\w+)',r'\1@\2.\3', i ))           #change the masked form to regular and add it to the list
    l5 = re.findall(r'\w+\[at\]\w+\[dot\]\w+', page)
    for i in l5:
        email_addresses.append(re.sub(r'(\w+)\[at\](\w+)\[dot\](\w+)',r'\1@\2.\3', i))            #change the masked form to regular and add it to the list
    email_addresses = list(set(email_addresses))                #remove any duplicates by converting it into and set and back into a list
    return email_addresses
    
    
#y = findemail("https://www.math.ucla.edu/~hangjie/teaching/Winter2019PIC16/regexTest")
#print y
    
def happiness(text):
    text = re.sub(r'[^\w\s]', '', text) #remove punctuation from the sentence
    words_in_text = text.split()        #create a list of words in the sentence
    word_count = 0
    total_value = 0
    for i in words_in_text:
        i = i.lower()
        value = hp.get(i, 0)            #check if the word is there in the dictionary
        if value == 0:
            continue                    #if not, move on to the next word
        else:
            total_value = total_value + value   #if the word is there, add it to the total value
            word_count = word_count + 1         #keep track of the count of words
    if word_count == 0:                         #if no words are in the dictionary, return 0
        return 0
    average_value = total_value/word_count
    return average_value                        #return the average value
          

#b = happiness('A quick brown fox jumps over a lazy dog.')
#print b

    
    

    

    
    

    
    
    
    
    


    
    