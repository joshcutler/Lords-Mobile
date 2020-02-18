# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:53:28 2019

@author: karthick
"""

import pyautogui
import time
import cv2

#import subprocess

time.sleep(2)

position = pyautogui.locateOnScreen('D:/Automation/lords_images/stone.png', confidence=0.8)
print(position)

pyautogui.moveTo(position, duration=0.01)#Moves the mouse to the coordinates of the image


im = pyautogui.screenshot('position.png', region=(850,420, 75, 50))

#print(pytesseract.image_to_string(Image.open('position.png')))
