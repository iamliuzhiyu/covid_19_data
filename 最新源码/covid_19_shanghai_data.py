from PIL import ImageGrab
from selenium import webdriver
import time, datetime
import os
driver = webdriver.Edge()
driver.get('file:///C:/covid_19_data/data.html')
time.sleep(20.0)
bbox = (37, 269, 1316, 1665)
im = ImageGrab.grab(bbox)
filename = "COVID-19." + str(datetime.date.today()) + ".png"
im.save('C:\\covid_19_data\\datas\\' + filename) # 把这里的路径换成你自己的路径
print("截图完成！")
os.system("python C:\\covid_19_data\\weixin.py")