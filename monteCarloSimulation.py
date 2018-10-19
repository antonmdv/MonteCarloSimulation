
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:33:24 2017

@author: antonmdv
"""

import timeit
import random
import math

start = timeit.default_timer()

n = 100000000
inCircle = 0


for i in range(n):
    x = random.random()
    y = random.random()
    
    d = math.sqrt(x**2 + y**2)
    
    if d <= 1:
        inCircle += 1
    
pi = inCircle/n * 4

stop = timeit.default_timer()

print('N value => ',n)
print('Pi => ',pi) 
print('Runtime => ', (stop - start),' seconds')