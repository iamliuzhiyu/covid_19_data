from PIL import ImageGrab
from selenium import webdriver
import time, datetime
import os
import pyautogui
configfile = open("C:\\covid_19_data\\config.ini")
outputpath = str(configfile.read())
configfile.close()
driver = webdriver.Edge()
driver.get('file:///C:/covid_19_data/data.html')
time.sleep(20.0)
pyautogui.press("f11")
im = pyautogui.screenshot()
pyautogui.press("f11")
filename = "COVID-19." + str(datetime.date.today()) + ".png"
im.save("C:\\Windows\\Temp\\covid_19_data\\" + filename)
filepath = "C:\\Windows\\Temp\\covid_19_data\\" + filename
write = open("C:\\covid_19_data\\filepath.ini", "w")
write.write(filepath)
write.close()
im.save(outputpath + filename)
print("截图完成！")
os.system("python C:\\covid_19_data\\weixin.py")

