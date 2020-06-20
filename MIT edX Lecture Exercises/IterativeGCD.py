# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:29:34 2020
Iterative way of finding the greatest common denominator
@author: Jun
"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    testA = a
    testB = b
    while True:
        if b % a == 0:
            gcd = a
            break
        elif a % b == 0:
            gcd = b
            break
        elif b > a:
            testA = testA - 1
            if b % testA == 0 and a % testA == 0:
                gcd = testA
                break
        else:
            testB = testB - 1
            if a % testB == 0 and b % testB == 0:
                gcd = testB
                break
    return gcd
            

                
        