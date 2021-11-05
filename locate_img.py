import cv2
import pyautogui
import win32gui, win32con
import os

def imgLocate(tempFile,  debug=False): #返回目标中心坐标
    '''
        tempFile :需要匹配的小图
        whatDo  :需要的操作
                pyautogui.moveTo(w/2, h/2)# 基本移动
                pyautogui.click()  # 左键单击
                pyautogui.doubleClick()  # 左键双击
                pyautogui.rightClick() # 右键单击
                pyautogui.middleClick() # 中键单击
                pyautogui.tripleClick() # 鼠标当前位置3击
                pyautogui.scroll(10) # 滚轮往上滚10， 注意方向， 负值往下滑
        更多详情：https://blog.csdn.net/weixin_43430036/article/details/84650938
        debug   :是否开启显示调试窗口
    '''
    # 读取屏幕，并保存到本地
    pyautogui.screenshot('big.png')
    # 读入背景图片
    gray = cv2.imread("big.png",0)
    # 读入需要查找的图片
    img_template = cv2.imread(tempFile,0)
    # 得到图片的高和宽
    w, h = img_template.shape[::-1]
    # 模板匹配操作
    res = cv2.matchTemplate(gray,img_template,cv2.TM_SQDIFF)

    # 得到最大和最小值得位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]

    top_left = min_loc #左上角的位置
    bottom_right = (top_left[0] + w, top_left[1] + h) #右下角的位
    '''
        # 先移动再操作， 进行点击动作，可以修改为其他动作
        pyautogui.moveTo(top+h/2, left+w/2)
        whatDo(x)
    '''
    if debug:
        # 读取原图
        img = cv2.imread("big.png",1)
        # 在原图上画矩形
        cv2.rectangle(img,top_left, bottom_right, (0,0,255), 2)
        # 调试显示
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
        cv2.imshow("processed",img)
        cv2.waitKey(0)
        # 销毁所有窗口
        cv2.destroyAllWindows()
    os.remove("big.png")
    return (int(top+w/2), int(left+h/2))