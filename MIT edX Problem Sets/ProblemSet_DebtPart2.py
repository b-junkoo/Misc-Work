# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:23:32 2020

Calculates the fixed monthly payment needed to pay off credit card balance
within 12 months and prints the result.

Inputs:
    balance: outstanding balance on credit card
    annualInterestRate: annual interest rate in decimal form
    
@author: Jun
"""

payment = 0
balance = 3329
annualInterestRate = 0.2

# Loop adds $10 in payment until the balance <= 0 after 12 months
while True:
    ini_bal = balance                               # Resets initial balance
    payment += 10           
    month = 0
    while month < 12:                               # tests to see if payment 
        month += 1                                  # can be used to pay off 
        ini_bal = ini_bal - payment                 # balance after 12 months 
        interest = (annualInterestRate/12)*ini_bal
        ini_bal = ini_bal + interest
    if round(ini_bal, 2) <= 0:                      # breaks loop if monthly
        print("Lowest Payment:", payment)           # payment is sufficient
        break
    
