import pyautogui, time
import pyperclip
from PIL import ImageGrab
from PIL import Image
import math
import operator

pyautogui.FAILSAFE = True
pyperclip.copy('修改日期：今天\n')
pyautogui.hotkey('ctrl', 'alt', 'w')
time.sleep(5.0)
pyautogui.moveTo(1912, 1189)
pyautogui.click()
print("请打开手机微信确认电脑版登录。")
time.sleep(30.0)
login = input("是否登陆成功？")

if login == "y":
    time.sleep(5.0)
    pyautogui.moveTo(1302, 522)
    pyautogui.click()
    time.sleep(0.5)
    qun = input("要发送的群\\联系人：")
    pyautogui.typewrite(qun)
    time.sleep(5.0)
    pyautogui.moveTo(1378, 685)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(1816, 1381)
    pyautogui.click()
    time.sleep(0.5)
    time.sleep(2.0)
    pyautogui.moveTo(1212, 823)
    time.sleep(0.5)
    pyautogui.scroll(-1000)
    time.sleep(0.5)
    pyautogui.moveTo(1232, 1027)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(1648, 547)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite('C:\\covid_19_data\\datas\\') # 把这里的路径换成前面一个文件里全球数据的存储位置
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.moveTo(2068, 545)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.moveTo(1515, 754)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(1976, 1292)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    print("发送成功！")
exit()