import pyautogui, time
import pyperclip
import math
sendto = input("发送给（可选多个，以;分隔）：").replace("@", '@').replace("；", ";").split(";")
pathf = open("C:\\covid_19_data\\filepath.ini")
path = str(pathf.read())
pyautogui.FAILSAFE = True
pyautogui.hotkey("win", "r")
time.sleep(0.5)
write = "mspaint" + path
pyautogui.typewrite(write)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "a")
time.sleep(0.5)
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)
pyautogui.hotkey('win', 's')
time.sleep(1.0)
pyautogui.typewrite("youjian")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(5.0)
pyautogui.hotkey("ctrl", "n")
time.sleep(0.5)
for text in sendto:
    pyautogui.typewrite(text.replace(";", ""))
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
for i in 1,3:
    pyautogui.press("tab")
    time.sleep(0.5)
pyautogui.typewrite("COVID-19 Data Today")
pyautogui.press("tab")
pyautogui.hotkey("ctrl", "v")
print("发送成功")
