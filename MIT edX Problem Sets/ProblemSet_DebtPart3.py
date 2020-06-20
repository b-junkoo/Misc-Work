# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:26:46 2020

Uses bisection search to return a fixed monthly payment to pay off debt in 12 months

@author: Jun
"""
balance = 999999
annualInterestRate = 0.18

monthlyInterest = annualInterestRate/12
low = balance/12
high = (balance * (1 + monthlyInterest)**12)/12
payment = (high+low)/2

while True:
    month = 0
    unpaid = balance
    while month < 12:                                   
        month += 1                                  
        unpaid = unpaid - payment                  
        interest = (annualInterestRate/12)*unpaid
        unpaid = unpaid + interest
    if unpaid < 0.01 and unpaid > -0.01:
        print("Lowest Payment:", round(payment, 2))
        break
    elif unpaid > 0:
        low = payment
        payment = (high+low)/2   
    elif unpaid < 0:
        high = payment
        payment = (high+low)/2
        
