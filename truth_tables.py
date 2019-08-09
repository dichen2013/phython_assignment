""" File name:   truth_tables.py
    Author:      <Di Chen>
    Date:        <March 9>
    Description: This file defines a number of functions which implement Boolean
                 expressions.
                 
                 It also defines a function to generate and print truth tables
                 using these functions.
                 
                 It should be implemented for Exercise 2 of Assignment 0.
                 
                 See the assignment notes for a description of its contents.
"""
def boolean_fn1(a, b, c):
    return not (a or b) or ((not a) and (not b))

def boolean_fn2(a, b, c):
    return (a and b) or ((not a) and (not b))

def boolean_fn3(a, b, c):
    return ((not c or a) and (a and (not b))) or (not a and b)

def draw_truth_table(boolean_fn):
    """ This function prints a truth table for the given boolean function.
        It is assumed that the supplied function has three arguments.

        ((bool, bool, bool) -> bool) -> None
    """
    if boolean_fn==1:
        print("True")
    else:
        print("False")
