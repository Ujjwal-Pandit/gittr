# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:24:04 2020

@author: DELL
"""
'''Calculates the number of times the sum of the randomly
 rolled dice equals each possible value from 2 to 12.
 Repeatedly asks the user for the number of times to roll
 the dice, quitting only when the user-entered number is
 less than 1. 
 Hint: Use a while loop that will execute
 as long as num_rolls is greater than 1.
 Prints a histogram in which
 the total number of times the dice
 rolls equals each possible value is displayed
 by printing a character, such as *, that number of times.'''

import random
num_2 = ''
num_3 = ''
num_4 = ''
num_5 = ''
num_6 = ''
num_7 = ''
num_8 = ''
num_9 = ''
num_10 = ''
num_11 = ''
num_12 = ''
x = 0

num_roll = int(input("Enter the number of rolls:\n"))

if num_roll >= 1:
    while x in range(num_roll):
        die1 = random.randint(1,7)
        die2 = random.randint(1,7)
        tot = die1 + die2
        
        if tot == 2:
            num_2 += ''+'*'
        if tot == 3:
            num_3 += ''+'*'
        if tot == 4:
            num_4 += ''+'*'
        if tot == 5:
            num_5 += ''+'*'
        if tot == 6:
            num_6 += ''+'*'
        if tot == 7:
            num_7 += ''+'*'
        if tot == 8:
            num_8 += ''+'*'
        if tot == 9:
            num_9 += ''+'*'
        if tot == 10:
            num_10 += ''+'*'
        if tot == 11:
            num_11 += ''+'*'
        if tot == 12:
            num_12 += ''+'*'
        x += 1
    
    print ('\nDice Roll Histogram \n')
    
    print('2s: {}'.format(num_2))
    print('3s: {}'.format(num_3))
    print('4s: {}'.format(num_4))
    print('5s: {}'.format(num_5))
    print('6s: {}'.format(num_6))
    print('7s: {}'.format(num_7))
    print('8s: {}'.format(num_8))
    print('9s: {}'.format(num_9))
    print('10s: {}'.format(num_10))
    print('11s: {}'.format(num_11))
    print('12s: {}'.format(num_12))
    
else:
    print('Invalid number of rolls. Try again.')