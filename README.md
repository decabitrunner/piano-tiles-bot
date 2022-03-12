# piano tiles bot

A easy piano tiles bot to prove a point

## Why even post such a simple project?

The reason why I have decided to post this project simplifies down to these __points:__

* I want to play around with markdown more
* I've seen videos on youTube and understood that their audience may not be aware of how simple it is
* To know how to teach even the simplist things

## A full dive into [main.py](https://github.com/decabitrunner/piano-tiles-bot/blob/main/main.py)

### What libreries do we need and why?

```python
from pyautogui import *
import pyautogui as ag
import time
import keyboard
import win32api, win32con
```

1. __PyautoGUI__ - This is a library that we will be using to detect pixels on the screen.
2. __Time__ - we use to preform basic time functions like waiting.
3. __Keyboard__ - used to provide a way of quitting the program easily, as in onclick()
4. __win32api__ - a windows api which lets us simulate clicks
5. __win32con__ - another windows api which we use to emulate mouse movment

### The click function

```python
def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.0001)
```
This function takes in the x, y cordinates of a pixel.
