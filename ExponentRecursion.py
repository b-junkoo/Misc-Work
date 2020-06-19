# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:42:33 2020

Recursive way of expressing exponents

@author: Jun
"""

def recPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base*recPower(base, (exp-1))

