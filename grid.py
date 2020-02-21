# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:06:30 2020

@author: karth
"""

import numpy as np
import pyautogui
import time
from num2words import num2words 


x = 510
y = 1010

increment = 10

matrix = np.empty((x,y))

total_x = []
total_y = []

val_index = []

grid = []

Map_Pos = 960,140
X_Pos = 960,390
Y_Pos = 1170, 390
Close_Pos = 1250,190
Go_pos = 960, 550
tick = 1485, 725

time.sleep(5)

def giveCoords(num):
    #numeric keyboard position
    if num == 'one':
        return 1300, 440
    elif num == 'two':
        return 1430, 440
    elif num == 'three':
        return 1560,440
    elif num =='four':
        return 1300, 535
    elif num =='five':
        return 1430, 535
    elif num =='six':
        return 1560, 535
    elif num =='seven':
        return 1300, 630
    elif num =='eight':
        return 1430, 630
    elif num =='nine':
        return 1560, 630
    elif num =='zero':
        return 1340, 725

for i in range(5, x, increment):
    #Click Close if map for opens already
    pyautogui.click(Close_Pos)
    time.sleep(1)
    pyautogui.click(Map_Pos)
    time.sleep(1)    
    pyautogui.click(X_Pos)
    time.sleep(1)
    x_list = [int(a) for a in str(i)]
    print(x_list)
    for xp in x_list:
        print(xp)
        c_n_x = num2words(xp)
        pyautogui.click(giveCoords(c_n_x))
        time.sleep(1)
    pyautogui.click(tick)
    time.sleep(1)

    for j in range(5, y, increment):
        coords = i,j
        print(coords)
        pyautogui.click(Y_Pos)
        time.sleep(1)
        y_list = [int(b) for b in str(j)] 
        for yp in y_list:
            c_n_y = num2words(yp)
            pyautogui.click(giveCoords(c_n_y))
            time.sleep(1)
        pyautogui.click(tick)
        time.sleep(1)
        pyautogui.click(Go_pos)
        time.sleep(1)
        file_name = str(i)+"_"+str(j)+".png"
        pyautogui.screenshot(file_name)
        time.sleep(2)
        pyautogui.click(Close_Pos)
        time.sleep(1)
        pyautogui.click(Map_Pos)
        time.sleep(1)
            
