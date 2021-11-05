import pyautogui
import time
import random


# 保护措施，避免失控
pyautogui.FAILSAFE = True
# 为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
pyautogui.PAUSE = 0.3
notex, notey = 465, 1060

# pyautogui.click(1805,15) # 最小化ide
time.sleep(0.5)
while 1:
    try:
        pyautogui.click(100, 25, duration=0.5)
        pyautogui.moveTo(760, 540, duration=0.5)
        bt = pyautogui.locateOnScreen("./img/01sec_bt2.png")
        if bt == None:
            bt = pyautogui.locateOnScreen("./img/02sec_bt1.png")
        if bt == None:
            pyautogui.scroll(-random.randint(100, 150))
            a = []
            print(666)
            a[100]
        (x, y) = pyautogui.center(bt)
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()
        pyautogui.moveTo(x+100, y, duration=0.3)
        pyautogui.click()
        time.sleep(19)
        bt = pyautogui.locateOnScreen('./img/bigger.png')
        if bt == None:
            x, y = 760, 540
        else:
            (x, y) = pyautogui.center(bt)
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
        time.sleep(3)
        bt = pyautogui.locateOnScreen('./img/long.png')
        if bt == None:
            x, y = 760, 540
        else:
            (x, y) = pyautogui.center(bt)
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
        (x, y) = 1345, 335
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.dragTo(x-1200, y, duration=0.8)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.moveTo(notex, notey, duration=0.8)
        pyautogui.click()
        pyautogui.moveTo(1465, 1005, duration=0.3)
        pyautogui.typewrite("<p>\n<title>\n")
        pyautogui.hotkey("ctrl", 'v')
        pyautogui.typewrite("\n</title>\n")
        pyautogui.moveTo(200, 300, duration=0.5)
        pyautogui.click()
        pyautogui.scroll(-random.randint(150, 180))
        #bt = locate_img.imgLocate('./img/04refs.png')
        isFound = 0
        times = 0
        while isFound == 0:
            time.sleep(0.2)
            bt = pyautogui.locateOnScreen("./img/04refs.png", confidence=0.65)
            if bt != None:
                isFound = 1
                (x, y) = pyautogui.center(bt)
                pyautogui.scroll(-100)
                bt = pyautogui.locateOnScreen(
                    "./img/04refs.png", confidence=0.65)
                (x, y) = pyautogui.center(bt)
                pyautogui.moveTo(x, y+30, duration=0.2)
                pyautogui.click()
                break
            pyautogui.scroll(-random.randint(190, 220))
            times += 1
            if times > 50:
                break
        if isFound == 0:
            break
        pyautogui.hotkey("ctrl", 'a')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.moveTo(notex, notey, duration=0.8)
        pyautogui.click()
        pyautogui.moveTo(1465, 1005, duration=0.3)
        pyautogui.typewrite("<ref>\n")
        pyautogui.hotkey("ctrl", 'v')
        pyautogui.typewrite("\n</ref>\n</p>\n\n")
        pyautogui.moveTo(370, 25, duration=0.5)
        pyautogui.middleClick()
    except:
        continue
