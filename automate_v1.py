# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:18:51 2019

@author: karth
"""

import subprocess
import pyautogui
import time


#get into lords mobile
#pyautogui.hotkey('win','s')
#pyautogui.typewrite('Lords Mobile', interval=0.1)
#pyautogui.press('enter')

time.sleep(7)

print(pyautogui.size())

time.sleep(3)
#make sure you hit the center position and click your castle
pyautogui.moveTo(1700, 520)
#drag left side
pyautogui.dragTo(300, 400, 1, button='left')
time.sleep(3)
#click gotoposition
pyautogui.click(1630, 310)
time.sleep(1)
#click on castle
pyautogui.click(950,540)
time.sleep(1)
#click on enter turf
pyautogui.click(950, 640)
time.sleep(1)

helps = 40
for click in range(helps):
    #click on food farm
    pyautogui.click(950,540)
    time.sleep(0.5)
    #click to upgradebutton
    pyautogui.click(1480,920)
    time.sleep(0.5)
    #click upgrade again
    pyautogui.click(1480,920)
    time.sleep(0.5)
    #click on farm again
    pyautogui.click(950,540)
    time.sleep(0.5)
    #click on help
    pyautogui.click(1480,920)
    time.sleep(3)
    #click on farm again
    pyautogui.click(950,540)
    time.sleep(0.5)
    #click on cancel
    pyautogui.click(1300,920)
    time.sleep(0.5)
    #click on cancel confirm
    pyautogui.click(1150,550)
    time.sleep(1)

pyautogui.hotkey('alt', 'tab', 'tab')
