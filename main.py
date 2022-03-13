from pyautogui import *
import pyautogui as ag
import time
import keyboard
import win32api, win32con



def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.0001)

time.sleep(3)
y = 700
while keyboard.is_pressed('q') == False:

    if ag.pixel(745, y)[0]  == 0:
        click(745, y)

    if ag.pixel(876, y)[0] == 0:
        click(876, y)

    if ag.pixel(1046, y)[0] == 0:
        click(1046, y)

    if ag.pixel(1212, y)[0] == 0:
        click(1212, y)
