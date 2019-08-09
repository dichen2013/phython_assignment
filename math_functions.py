""" File name:   math_functions.py
    Author:      <Di Chen>
    Date:        <March 9>
    Description: This file defines a set of variables and simple functions.
                 
                 It should be implemented for Exercise 1 of Assignment 0.
                 
                 See the assignment notes for a description of its contents.
"""
# 1
import math
ln_e = math.exp(1)

# 2
twenty_radians =20*math.pi/180.0

# 3
def quotient_ceil(x,y):
    return math.ceil(x/y)
def quotient_floor(x,y):
    return math.floor(x/y)

# 4
def manhattan(x1,y1,x2,y2):
    return abs(x1-x2)+abs(x2-y2)



