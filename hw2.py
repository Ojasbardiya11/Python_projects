#!/usr/bin/env python2
# -*- coding: utf-8 -*-

##Created on Tue Oct 15 18:33:32 2019

##@author: ojasbardiya

import math

##some dictionaries used as test cases

d1 = dict()
d1["a"] = "b"
d1["b"] = "c"

d2 = dict()
d2["a"] = "b"
d2["b"] = "c"
d2["c"] = "d"
d2["e"] = "a"
d2["f"] = "a"
d2["d"] = "b"

d3 = dict()
d3["a"] = "b"
d3["b"] = "c"
d3["c"] = "d"
d3["d"] = "e"
d3["e"] = "c"
d3["f"] = "a"
d3["g"] = "f"
d3["h"] = "g"


def longestpath(d):
    maxlength = 0       ##declaring variables
    default = -1
    if len(d) <= 0:     ##case of empty dictionary
        return 0
    dict_elements = d.keys()  ##storing all keys in the dictionary in a list
    for i in dict_elements:   ##find path length for each key by looping
        cur_length = 0
        values_seen = [i]
        cur_value = d.get(i, default)       
        while cur_value not in values_seen: ##until the same value is encountered twice, continue along the current path
            if cur_value == default:        ##if there is no value for the corresponding key exit the loop
                break
            values_seen.append(cur_value)   ##add the current value to the list of values already passed along the path
            cur_length = cur_length + 1
            cur_value = d.get(cur_value, default) ##move on to the next value
            if cur_value in values_seen and cur_value != default: ##to make sure the step taken to get to a value already passed by is included
                cur_length = cur_length + 1
        if cur_length > maxlength:
            maxlength = cur_length
    return maxlength  ##return the length of the longest path

##x = longestpath(d3)
##print x
    

## test case for second function

func = lambda x: [math.exp(x) - 1, math.exp(x)]

    
def solve(function, x, e):
    x = float(x)
    error = float(function(x)[0])      ##function
    if abs(error) <= e:                ## if the first estimate satisifies the bounds return it
        return x
    else:
        while abs(error) > e:          ##until the estimate satisfies the bounds, continue the algorithm
            f = float(function(x)[0])  ##function itself
            df = float(function(x)[1]) ##derivate of function
            x = x - f/df
            error = float(function(x)[0])  ##next estimate
    return x 

##print solve(func, 1, 0.0001)

    
    
    
    
    

           


    
        


 

