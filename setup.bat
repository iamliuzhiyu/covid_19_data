set http_proxy=http://127.0.0.1:1080
cd %HOMEPATH%\AppData\Local\Programs\Python\Python38\Scripts\
pip install whell
pip install pyautogui
pip install selenium
pip install Pillow
pip install tkinter
cd C:\
mkdir covid_19_data
cd covid_19_data
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/iamliuzhiyu/covid_19_data/master/covid_19_data/config.json -OutFile config.json"
cd C:\Temp\
mkdir covid_19_data