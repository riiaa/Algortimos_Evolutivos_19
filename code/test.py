#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 07:36:15 2018

@author: stan
"""

import random

x = random.randint(0,1<<1000000)

def count_ones(number):
    c = 0
    while(number !=0 ):
        number = number&(number-1)
        c = c + 1
    return c


%timeit bin(x).count("1")
%timeit count_ones(x)