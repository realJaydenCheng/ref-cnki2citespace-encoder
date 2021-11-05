from ctypes import py_object
import pyautogui
import time
import random

from pyscreeze import locateOnScreen

#保护措施，避免失控
pyautogui.FAILSAFE = True
#为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
pyautogui.PAUSE = 0.3

#pyautogui.click(1805,15) # 最小化ide
time.sleep(0.5)
for i in range(350):
    try :
        pyautogui.moveTo(760,540,duration=0.5)
        bt = pyautogui.locateOnScreen("./img/01sec_bt2.png")
        if bt == None : 
            bt = pyautogui.locateOnScreen("./img/02sec_bt1.png")
        if bt == None :
            pyautogui.scroll(-random.randint(30,50))
            a = [] 
            a[100]
        (x,y) = pyautogui.center(bt)
        pyautogui.moveTo(x,y,duration=0.5)
        pyautogui.click()
        pyautogui.moveTo(x+100,y,duration=0.3)
        pyautogui.click()
        time.sleep(20)
        bt = pyautogui.locateOnScreen('./img/bigger.png')
        if bt == None :
            x , y = 760 , 540
        else :
            (x,y) = pyautogui.center(bt)
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()
        time.sleep(3)
        bt = pyautogui.locateOnScreen('./img/long.png')
        if bt == None :
            x , y = 760 , 540
        else :
            (x,y) = pyautogui.center(bt)
            pyautogui.moveTo(x,y,duration=0.5)
            pyautogui.click()
        (x,y) = 1345 , 335
        pyautogui.moveTo(x,y,duration=0.5)
        pyautogui.dragTo(x-1200,y,duration=0.8)
        pyautogui.hotkey('ctrl','c')
        pyautogui.moveTo(560,1060,duration=0.8)
        pyautogui.click()
        pyautogui.moveTo(1465,1005,duration=0.3)
        pyautogui.typewrite("<p>\n<title>\n")
        pyautogui.hotkey("ctrl",'v')
        pyautogui.typewrite("\n</title>")
        pyautogui.moveTo(200,300,duration=0.5)
        pyautogui.click()
        foundRef = 0
        while(foundRef == 0):
            pyautogui.scroll(random.randint(30,50))
            bt = pyautogui.locateOnScreen('./img/04refs.png')
            if bt == None :
                continue
            

        
    except:
        continue
