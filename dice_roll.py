# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:08:17 2022

@author: VARUN
"""

import random

def roll_dice():
    
    
    
    roll = input("Roll the dice? (Yes/No): ")
    
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        print("dice rolled: {} and {}".format(dice1, dice2))
        
        roll = input("Roll again? (Yes/No): ")
        
roll_dice()