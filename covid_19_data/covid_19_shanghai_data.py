from PIL import ImageGrab
from selenium import webdriver
import time, datetime
import os
import json
configfile = open("C:\\covid_19_data\\config.json")
config = configfile.read().json
outputpath = config["outputpath"]
driver = webdriver.Edge()
driver.get('file:///C:/covid_19_data/data.html')
time.sleep(20.0)
bbox = (37, 269, 1316, 1665)
im = ImageGrab.grab(bbox)
filename = "COVID-19." + str(datetime.date.today()) + ".png"
im.save(outputpath + filename)
print("截图完成！")
os.system("python C:\\covid_19_data\\weixin.py")
