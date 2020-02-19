# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:06:30 2020

@author: karth
"""

import numpy as np
import pyautogui
import time
from num2words import num2words 


x = 20 #510
y = 40 #1010

increment = 10

matrix = np.empty((x,y))

total_x = []
total_y = []

val_index = []

grid = []

X_Pos = 960,390
Y_Pos = 1170, 390


#numeric keyboard position
one = 1300, 440
two = 1430, 440
three = 1560,440
four = 1300, 535
five = 1430, 535
six = 1560, 535
seven = 1300, 630
eight = 1430, 630
nine = 1560, 630
zero = 1340, 725
tick = 1485, 725

time.sleep(5)



for i in range(5, x, increment):
    pyautogui.click(X_Pos)
    time.sleep(0.5)
    
    x_list = [int(a) for a in str(x)] 
    
    for xp in x_list:
        c_n_x = num2words(xp)
        print(c_n_x)
        #pyautogui.click(c_n_x)
    #pyautogui.click(tick)
    for j in range(5, y, increment):
        coords = i,j
        #pyautogui.click(Y_Pos)
        y_list = [int(b) for b in str(x)] 
        for yp in y_list:
            c_n_y = num2words(yp)
            print(c_n_y)
            #pyautogui.click(c_n_y)
        #pyautogui.click(tick)
            
            
