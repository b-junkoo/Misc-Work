# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:33:10 2020
sums the perimeter squared and area of any regular polygon
@author: Jun
"""
import math
def polysum(n,s):
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    peri = (n*s)**2
    sum = round(area + peri, 4)
    return sum