#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:27:08 2017

@author: merclan
"""

"""
Problem 2_4:
random.random() generates pseudo-random real numbers between 0 and 1. But what
if you needed other random reals? Write a program to use only random.random()  
to generate a list of random reals between 30 and 35. This is a simple matter
of multiplication and addition. By multiplying you can spread the random numbers
out to cover the range 0 to 5. By adding you can shift these numbers up to the 
required range from 30 to 35.  Set the seed in this function to 70 so that 
everyone generates the same random numbers and will agree with the grader's 
list of random numbers. Print out the list (in list form).
"""
#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    r = []
    random.seed(70)
    for i in range(10):
        r.append(random.random()*5+30)
    print(r)

#%%
"""
COMMENT: Note that this uses a pseudorandom number generator.  That means
that the list will be different for each person.  We issue the command 
random.seed(70) inside the function problem2_4() to insure that we generate the
same numbers that the grader expects. If you do this problem correctly, you 
should get the list of random numbers below.

Test run:

problem2_4()
[34.54884618961936, 31.470395203793395, 32.297169396656095, 30.681793552717807,
 34.97530360173135, 30.773219981037737, 33.36969776732032, 32.990127772708405, 
 33.57311858494461, 32.052629620057274]
"""