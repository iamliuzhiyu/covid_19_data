![题图](https://github.com/iamliuzhiyu/datas/blob/master/%E9%A2%98%E5%9B%BE.png)

# 用selenium和pyautogui模块实现Python自动截取新冠肺炎疫情上海、全球数据图片

前几天突发奇想，想用Python实现自动截取新冠肺炎疫情数据并发到微信群。

首先，用edgedriver驱动MSEdge（chromedriver没有canary版），

edgedriver[下载](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

注意下载后要解压然后拷到python根目录然后重启电脑。

下面的也是一样的安装完了要重启。

然后安装selenium。

这一步要挂梯子！

要挂梯子！

挂梯子！

（重要的事情说三遍！）

挂梯子方法：

命令行输入：
```
set http_proxy=localhost:1080 # 把1080换成你自己电脑的代理端口
```
然后下载安装`selenium`：
```
pip install selenium
```
第一次运行会报错，多试几次，还是不行那就等会儿运行。

提示`Sucsessful installed selenium`就说明安装成功。

还有，上面挂梯子的代码关掉命令行窗口之后就会失效。

然后安装`pyautogui`：

先`cd`进`python`根目录下的`Scripts`：
```
cd C:\Users\yourusername\AppData\Local\Programs\Python\Python38\Scripts\
# 把yourusername换成你的用户名
```
然后先安装一个`pyautogui`依赖的库：`whell`（一定要在这个目录下运行）
```
pip install whell
```
安装好后安装`pyautogui`：
```
pip install pyautogui
```
上面几个命令都要挂梯子，挂梯子方法看上边👆

然后开始敲代码：

首先引入：

我这里是两个功能分两个文件，所以要实现自动化就得第一个文件之后自动执行第二个文件，要引入os。
```
from PIL import ImageGrab
from selenium import webdriver
import time, datetime
import os
```
对了忘说了这之前得再安装个Pillow，就是上面的PIL：
```
pip install Pillow
```
然后是驱动`edge`访问这个网址：https://www.http://bing.com/covid/local/shanghai_chinamainland?form=WSHCOV， 是新冠肺炎疫情上海数据的网址：
```
driver = webdriver.Edge()
driver.get('https://www.bing.com/covid/local/shanghai_chinamainland?form=WSHCOV')
time.sleep(20.0)
```
time.sleep是网页的反应时间，我测了几遍，基本上20秒是能加载出来的。

下面开始截图：
```
bbox = (748, 588, 1345, 1091)# 设置截图范围
im_sh = ImageGrab.grab(bbox)# 截取上海图片
bbox = (60, 411, 632, 873)# 再次设置截图范围
im_wd = ImageGrab.grab(bbox)# 截取全球图片
```
下面就是保存图片：
```
# 设置文件名
sh_filename = "COVID-19.Shanghai." + str(datetime.date.today()) + ".png"
wd_filename = "COVID-19.World." + str(datetime.date.today()) + ".png"

# 保存文件
im_sh.save('E:\\covid19_data\\Shanghai\\' + sh_filename)
im_wd.save('E:\\covid19_data\\World\\' + wd_filename)
# 上面文件名和路径改成你自己的文件名和路径
```
截图和保存都完成了，别忘了提示一下：
```
print("截图完成！")
```
下面就是自动执行登陆微信+发微信：
```
os.system('python "['weixin.py'路径]"') # 注意这里要改一下
# os.system()可以将括号内的内容发送到系统终端
```
好了，第一个文件编好了，下面贴上第一个文件全部代码：
```
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
# 上面文件名和路径改成你自己的文件名和路径
print("截图完成！")

os.system('python "E:\\python_study\\py\\covid-19-shanghai-data\\weixin.py"')
# 上面路径改成你自己的路径
```
---
这里是第二个文件啦，只要截图保存的退出吧。

引入：
```
import pyautogui, time
# pyautogui用于控制鼠标和键盘，time用于等待程序响应
```
加上保护机制：
```
pyautogui.FAILSAFE = True
# 这个FAILSAFE属性是一个保护机制，将它设为True之后如果鼠标移到左上角就会停止程序
```
启动微信：
```
pyautogui.hotkey('ctrl', 'alt', 'w')
time.sleep(5.0)
# 上面的等待是等微信启动，一般需要几秒的
```
点击登录按钮：
```
pyautogui.moveTo(1912, 1189)# 移动鼠标
pyautogui.click()# 点击
```
提示确认登录：
```
print("请打开手机微信确认电脑版登录。")
```
等待登录成功：
```
login = input("是否登陆成功？(y/n)")
```
等用户切换到微信窗口：
```
time.sleep(5.0)
```
点击搜索框：
```
pyautogui.moveTo(1302, 522)
pyautogui.click()
```
键入搜索字词（中文不可以）：
```
pyautogui.typewrite('群名称')
```
等待搜索完毕：
```
time.sleep(5.0)
```
移到第一个项目的位置+点击：
```
pyautogui.moveTo(1378, 685)
pyautogui.click()
```
点击打开文件按钮：
```
pyautogui.moveTo(1816, 1381)
pyautogui.click()
```
等待加载：
```
time.sleep(2.0)
```
回到根目录以防路径输入错误：
```
pyautogui.moveTo(1212, 823)
pyautogui.scroll(-1000)
pyautogui.moveTo(1232, 1027)
pyautogui.click()
```
在地址栏键入：
```
pyautogui.moveTo(1648, 547)
pyautogui.click()
pyautogui.typewrite('前面填的全球数据截图所在文件夹路径')
pyautogui.press('enter')
```
搜索当天编辑的文件：
```
pyautogui.moveTo(2068, 545)
pyautogui.click()
pyautogui.typewrite('修改日期：今天\n')
```
点击第一项：
```
pyautogui.moveTo(1515, 754)
pyautogui.click()
```
点击确定：
```
pyautogui.moveTo(1976, 1292)
pyautogui.click()
```
发送（好像不管用）：
```
pyautogui.press('enter')
```
退出脚本
```
exit()
```

好了，发送成功（上面的代码要粘两遍，第二遍路径改成上海数据截图）

这里贴上本次编写的全部代码：
```
# 第一个文件
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

# 下面是第二个文件的
import pyautogui, time
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
    exit()
```
最后的最后，连拷贝粘贴都懒得干的请[点这里](https://github.com/iamliuzhiyu/covid_19_data/releases).

对了，运行完了记得多按个回车。

***

# 使用说明

拆分版运行covid_19_shanghai_data.py即可

整合版直接运行整合版.py
