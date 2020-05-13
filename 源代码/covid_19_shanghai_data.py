from PIL import ImageGrab
from selenium import webdriver
import time, datetime
import os
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

os.system('python "E:\\python_study\\py\\covid-19-shanghai-data\\weixin.py"')