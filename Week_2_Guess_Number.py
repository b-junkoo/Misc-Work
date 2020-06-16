# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:40:38 2020

@author: Jun
"""
low = 0
high = 100
ans = round((high + low)/2)
print("Please think of a number between 0 and 100!")
user_input = ''
while user_input != 'c':  
    if user_input == 'h':
        high = ans
        ans = int((high + low)/2)
    elif user_input == 'l':
        low = ans
        ans = int((high + low)/2)
    print("Is your secret number", str(ans), "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_input not in ['h', 'l', 'c']:
        print("Sorry, I did not understand your input")
print("Game over. Your secret number was:", str(ans))