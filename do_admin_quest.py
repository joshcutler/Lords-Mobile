# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 23:36:00 2019
Bot Version : 0.2
Version Description: AutoFinich Guild and Admin Scrolls. 
@author: karthick
"""
import subprocess
import pyautogui
import time

#Define default aleep time for PyAutoGui
pyautogui.PAUSE = 0.8
#Define ScreenSize from PyAutoGui
screenWidth, screenHeight = pyautogui.size()

#Call Steam Application
#subprocess.call('C:\Program Files (x86)\Steam\Steam.exe')
#time.sleep(2)

#pyautogui.moveTo(250, 250)
#pyautogui.doubleClick()

time.sleep(3)

#move to scroll icon
pyautogui.moveTo(1220,1000, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.click()


quest_count = 6

for click in range(quest_count):
    #move position to admin scroll
    #Position of AdminScroll
    
    #assure admin scroll tab is open
    #Position of AdminScroll Heading x: 900, y: 220
    pyautogui.moveTo(870,220, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.moveTo(880, 310)
    pyautogui.click()
    pyautogui.moveTo(930, 640)
    pyautogui.click()   
    
    #total guild quest available for L60 castle
    count_of_adminScroll = 9
    
    #move to first quest position and start clicking 
    pyautogui.moveTo(1550,430)
    for click in range(count_of_adminScroll):
        pyautogui.click()
        time.sleep(0.8)

    
pyautogui.hotkey('alt', 'tab', 'tab')