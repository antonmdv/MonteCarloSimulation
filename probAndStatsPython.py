#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:01:03 2017

@author: antonmdv
"""

import scipy
import timeit

start = timeit.default_timer()

N=100000000

x_array = scipy.random.rand(N)
y_array = scipy.random.rand(N)

N_qtr_circle = sum(x_array**2+y_array**2 < 1) 
# Number of pts within the quarter circle x^2 + y^2 < 1 centered at the origin with radius
r=1. 
# True area of quarter circle is pi/4 and has N_qtr_circle points within it. 
# True area of the square is 1 and has N points within it, hence we approximate pi with 
pi_approx = 4*float(N_qtr_circle)/N 

stop = timeit.default_timer()

print('N value => ',N)
print('Pi => ',pi_approx) 
print('Runtime => ', (stop - start),' seconds')