#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:00:11 2017

@author: merclan
"""

""" 
Problem 2_8:
The following list gives the hourly temperature during a 24 hour day. Please
write a function, that will take such a list and compute 3 things: average
temperature, high (maximum temperature), and low (minimum temperature) for the
day.  I will test with a different set of temperatures, so don't pick out
the low or the high and code it into your program. This should work for
other hourly_temp lists as well. This can be done by looping (interating)
through the list. I suggest you not write it all at once. You might write
a function that computes just one of these, say average, then improve it
to handle another, say maximum, etc. Note that there are Python functions
called max() and min() that could also be used to do part of the jobs.
"""
#%%
hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]

def problem2_8(temp_list):
    print("Average:",sum(temp_list)/len(temp_list))
    print("High:",max(temp_list))
    print("Low:",min(temp_list))    
#%%
"""
Sample run using the list hourly_temp. Note that the grader will use a
different hourly list.  Be sure that you function works on this list and test
it on at least one other list of your own construction.
Note also, that the list the grader uses may not have the same number of items 
as this one.

problem2_8(hourly_temp)
Average: 38.791666666666664
High: 48.0
Low: 32.0
"""