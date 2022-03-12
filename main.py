from pyautogui import *
import pyautogui as ag
import time
import keyboard
import win32api, win32con

time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.0001)
y = 500
while keyboard.is_pressed('q') == False:

    if ag.pixel(745, 700)[0]  == 0:
        click(745, 700)

    if ag.pixel(876, 700)[0] == 0:
        click(876, 700)

    if ag.pixel(1046, 700)[0] == 0:
        click(1046, 700)

    if ag.pixel(1212, 700)[0] == 0:
        click(1212, 700)