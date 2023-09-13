import pyautogui
from urllib.request import urlopen
import time
import json

data_file = open("data.json")
data = json.load(data_file)
USER = data["USER"]
PASS = data["PASS"]
BROWSER_TASKBAR_LOCATION = str(data["BROWSER_TASKBAR_LOCATION"])


pyautogui.hotkey("win", BROWSER_TASKBAR_LOCATION)
time.sleep(3)
pyautogui.typewrite("http://172.16.0.30:8090/httpclient.html")
pyautogui.press("enter")
#t1 = time.time()
website = urlopen("http://172.16.0.30:8090/httpclient.html")
#t2 = time.time()
#print(t2-t1)
time.sleep(3)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.typewrite(USER)
pyautogui.press("tab")
pyautogui.typewrite(PASS)
pyautogui.press("enter")
time.sleep(7)
pyautogui.hotkey("ctrl", "w")
pyautogui.hotkey("ctrl", "t")
pyautogui.hotkey("ctrl", "pageup")
pyautogui.hotkey("ctrl", "w")

