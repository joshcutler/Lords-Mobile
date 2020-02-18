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
pyautogui.PAUSE = 2
#Define ScreenSize from PyAutoGui
screenWidth, screenHeight = pyautogui.size()

#Call Steam Application
subprocess.call('C:\Program Files (x86)\Steam\Steam.exe')
time.sleep(2)

pyautogui.moveTo(250, 250)
pyautogui.doubleClick()

time.sleep(6)

#move to scroll icon
pyautogui.moveTo(1220,1000, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.click()

#assure guild scroll tab is open
#Position of GuildScroll Heading x: 1220, y: 220
pyautogui.moveTo(1220,220, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.click()

#total guild quest available for L60 castle
count_of_guildScroll = 8

#move to first quest position and start clicking
pyautogui.moveTo(1550,430)
for click in range(count_of_guildScroll):
    pyautogui.click()
    #time.sleep(2.5)

#move position to admin scroll
#Position of AdminScroll

#assure admin scroll tab is open
#Position of AdminScroll Heading x: 900, y: 220
pyautogui.moveTo(900,220, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.click()

#total guild quest available for L60 castle
count_of_adminScroll = 9

#move to first quest position and start clicking 
pyautogui.moveTo(1550,430)
for click in range(count_of_adminScroll):
    pyautogui.click()
    time.sleep(2.5)

    
pyautogui.hotkey('alt', 'tab', 'tab')