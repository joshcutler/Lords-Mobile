# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:29:47 2019

@author: karth
"""

import cv2
import numpy as np
import pyautogui
import time

time.sleep(3)

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'tmp\castle.png')

img_src = cv2.imread(r'tmp\castle.png')
map_ = cv2.imread(r'clips\show_map.jpg')

w, h = map_.shape[:-1]

res = cv2.matchTemplate(img_src, map_, cv2.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(res >= threshold)
print(loc)
