# -*- coding: utf-8 -*-
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        gcd = a
        return gcd
    if a == 0:
        gcd = b
        return gcd
    elif a > b:
        rem = a % b
        a = b
        b = rem
        return gcdRecur(a, b)
    else:
        rem = b % a
        b = a
        a = rem
        return gcdRecur(a, b)
    
