# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:07:15 2020

Checks to see if number input is an Armstrong number and prints the result

@author: Jun
"""
def armstrong(num):
    num = str(num)
    if len(num) == 1:
        print(num, " is an Armstrong number.")
    else:
        numb = 0
        for n in num:
            numb += int(n)**len(num)
        if numb == int(num):
            print(num, "is an Armstrong number.")
        else:
            print(num, "is not Armstrong number.")
