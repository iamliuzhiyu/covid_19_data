'''
此文件在首次使用前需运行。
'''

import os, time
port = input("您电脑的代理端口是：")
os.system("set http_proxy=localhost:" + port)
for i in 1, 10:
    try:
        os.system("pip install selenium")
        time.sleep(300)
        print("正在安装selenium……如果提示successful installed selenium，请按Ctrl+C。")
    except KeyboardInterrupt:
        print("已安装selenium。")
for i in 1, 10:
    try:
        os.system("pip install Pillow")
        time.sleep(300)
        print("正在安装Pillow……如果提示successful installed Pillow，请按Ctrl+C。")
    except KeyboardInterrupt:
        print("已安装Pillow。")
user = input("请问您python安装路径是：（\\请用\\\\代替）")
os.system("cd " + user + "\\Script\\")
for i in 1, 10:
    try:
        os.system("pip install pyautogui")
        time.sleep(300)
        print("正在安装pyautogui……如果提示successful installed pyautogui，请按Ctrl+C。")
    except KeyboardInterrupt:
        print("已安装pyautogui。")
