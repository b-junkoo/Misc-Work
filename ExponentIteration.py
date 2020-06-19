# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:02:40 2020

@author: Jun
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    while exp != 0:
        exp = exp - 1
        result = result * base
    return(result)


