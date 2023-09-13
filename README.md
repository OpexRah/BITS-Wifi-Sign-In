# BITS-Wifi-Sign-In
An automatic wifi sign in tool for windows users who are too lazy to fill in the credentials every other day.

Like the title says, this application automatically logs you in for WiFi access in the BPHC campus. Inspired by the android version of the app, I have tried to make one for Windows users.
The application is written in python with very basic usage of ``pyautogui``, a library that can take control of your screen and perform clicks and key presses. 

## Installation
Clone this repo. All dependencies are included for the app to run. Refer to the next section for usage guide.

## How to use
Open the ``data.json`` file and fill in the credentials for ``USER`` and ``PASS``. ``BROWSER_TASKBAR_LOCATION`` is the position of your preferred browser in your taskbar. For example: If you have your Chrome browser in the second position in your taskbar (second from the left), put the value of ``2``. Now just click ``BITS Wifi Tool.exe`` and relax. You will automatically be signed in.

## Too Much Work To Click The .exe File?? Read this!
Now, you might be thinking that you have to put even more effort to click the .exe file everytime you want to login. I have a solution for that too!

1. Pin the .exe to your Start Menu and just click it from the menu when you want to sign in.
2. Create a shortcut of the .exe file and move it to ``C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup``. This will cause the app to run after you boot up your system, thus giving you a handsfree experience to connect to BITS Wifi while you are doing some other task.
