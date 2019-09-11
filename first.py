# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:36:01 2019
Bot Version : 0.1
Version Description: AutoFinich Guild and Admin Scrolls. 
@author: karthick
"""
import subprocess
import pyautogui
import time

#Define default aleep time for PyAutoGui
pyautogui.PAUSE = 2
#Define ScreenSize from PyAutoGui
screenWidth, screenHeight = pyautogui.size()
print(screenWidth)

#Call Steam Application
subprocess.call('C:\Program Files (x86)\Steam\Steam.exe')
time.sleep(2)

pyautogui.moveTo(250, 250)
pyautogui.doubleClick()

time.sleep(8)

pyautogui.moveTo(700, 80)
pyautogui.click()
pyautogui.moveTo(700, 980, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.typewrite('Gd ngt everyone', interval=0.25)
pyautogui.moveTo(1580, 980)
pyautogui.click()