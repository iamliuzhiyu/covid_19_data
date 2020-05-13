# 第一个文件
from PIL import ImageGrab
from selenium import webdriver
import time, datetime
driver = webdriver.Edge()
driver.get('https://www.bing.com/covid/local/shanghai_chinamainland?form=WSHCOV')
# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
time.sleep(20.0)
bbox = (748, 588, 1345, 1091)
im_sh = ImageGrab.grab(bbox)
bbox = (60, 411, 632, 873)
im_wd = ImageGrab.grab(bbox)
# 参数 保存截图文件的路径
sh_filename = "COVID-19.Shanghai." + str(datetime.date.today()) + ".png"
wd_filename = "COVID-19.World." + str(datetime.date.today()) + ".png"
im_sh.save('E:\\covid19_data\\Shanghai\\' + sh_filename)
im_wd.save('E:\\covid19_data\\World\\' + wd_filename)
print("截图完成！")


# 下面是第二个文件的
import pyautogui
pyautogui.FAILSAFE = True
pyautogui.hotkey('ctrl', 'alt', 'w')
time.sleep(5.0)
pyautogui.moveTo(1912, 1189)
pyautogui.click()
print("请打开手机微信确认电脑版登录。")
login = input("是否登陆成功？(y/n)")
if login == "y":
    time.sleep(5.0)
    pyautogui.moveTo(1302, 522)
    pyautogui.click()
    pyautogui.press(['5', '0', '2'])
    time.sleep(5.0)
    pyautogui.moveTo(1378, 685)
    pyautogui.click()
    pyautogui.moveTo(1816, 1381)
    pyautogui.click()
    time.sleep(2.0)
    pyautogui.moveTo(1212, 823)
    pyautogui.scroll(-1000)
    pyautogui.moveTo(1232, 1027)
    pyautogui.click()
    pyautogui.moveTo(1648, 547)
    pyautogui.click()
    pyautogui.typewrite('E:\\covid19_data\\World\\')
    pyautogui.press('enter')
    pyautogui.moveTo(2068, 545)
    pyautogui.click()
    pyautogui.typewrite('修改日期：今天\n')
    pyautogui.moveTo(1515, 754)
    pyautogui.click()
    pyautogui.moveTo(1976, 1292)
    pyautogui.click()
    pyautogui.press('enter')

    pyautogui.moveTo(1816, 1381)
    pyautogui.click()
    time.sleep(2.0)
    pyautogui.moveTo(1212, 823)
    pyautogui.scroll(-1000)
    pyautogui.moveTo(1232, 1027)
    pyautogui.click()
    pyautogui.moveTo(1648, 547)
    pyautogui.click()
    pyautogui.typewrite('E:\\covid19_data\\Shanghai\\')
    pyautogui.press('enter')
    pyautogui.moveTo(2068, 545)
    pyautogui.click()
    pyautogui.typewrite('修改日期：今天\n')
    pyautogui.moveTo(1515, 754)
    pyautogui.click()
    pyautogui.moveTo(1976, 1292)
    pyautogui.click()
    pyautogui.press('enter')
    print("发送成功！")