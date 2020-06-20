# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:55:24 2020

Credit card balance after one year

Input Variables: 
    balance - outstanding credit card balance
    annualInterestRate - annual interest rate in decimal form
    monthlyPaymentRate - minimum monthly payment rate as a decimal

Output Variables:
    balance - Changes to outstanding credit card balance at the end of the year
    
@author: Jun
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 0
while month < 12:
    month += 1
    balance = balance - balance*monthlyPaymentRate
    interest = (annualInterestRate/12)*balance
    balance = balance + interest
  
print("Remaining balance:", round(balance, 2))


        
        

    
        