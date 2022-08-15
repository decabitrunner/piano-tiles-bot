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
x_cords = [745,876,1046,1212]
while keyboard.is_pressed('q') == False:
  for cord in x_cords:
      if ag.pixel(cord, y)[0]  == 0:
          click(cord, y)
