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
This function takes in the x, y coordinates of a pixel.

```python
win32api.SerCursorPos((x, y))
```
we use win32api to set the cursor position (pased in a tuple)

```python
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
```
Now we can use win32con to press down the left mouse button on the cursor position that we set in the line above

```python
time.sleep(0.0001)
```
The reason we wait is because sometimes if there is no interval between the clicks they do not register.

### The main loop

```python
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
```

```python
time.sleep(3)
y = 700
```
We wait 3 seconds to give the user time to start the game after the script is ran.
than set y to be a constant becuase the clicks can be in the same height 

```python
while keyboard.is_pressed('q') == False:
```
We define a loop that will run until a keypress of 'q' is False

```python
if ag.pixel(745, y)[0]  == 0:
        click(745, y)
```
We check if the pixel with the color of (r, g, b)[0] (we can check for the first value becuase the rgb value of black is 0, 0, 0) is equal to 0
if yes we click it, for a better visulization you can look at hiw the game looks 

![alt text](https://github.com/decabitrunner/piano-tiles-bot/blob/main/res/to%20explain.PNG)

__and the click, visulize__

![alt text](https://github.com/decabitrunner/piano-tiles-bot/blob/main/res/visulized.PNG)

We do this for every four colums
```python
    if ag.pixel(745, y)[0]  == 0:
        click(745, y)

    if ag.pixel(876, y)[0] == 0:
        click(876, y)

    if ag.pixel(1046, y)[0] == 0:
        click(1046, y)

    if ag.pixel(1212, y)[0] == 0:
        click(1212, y)
```

## How to try it (if you want to)

### Get the cooardinates

To get cordinates on your screen you can use a usfull function,
``` python
pyautogui.displayMousePosition()
```
This will display the coordinates and rgb color of the pixel your cursor is on

The output will look something like this
``` 
Press Ctrl-C to quit.
X:  680 Y:  469 RGB: (255, 255, 255)
X: 1312 Y:  586 RGB: (  0,   0,   0)
X: 1218 Y:  278 RGB: (  0,   0,   0)
X: 1141 Y:  614 RGB: (  0,   0,   0)
X:  804 Y:  373 RGB: (255, 255, 255)
X:  270 Y:  551 RGB: (255, 255, 255)
X:  284 Y:  240 RGB: (  0,   0,   0)
X:  358 Y:  621 RGB: (255, 255, 255)
X:  203 Y:  526 RGB: (  0,   0,   0)
X:  193 Y:  659 RGB: (  0,   0,   0)
```

You can use this to find the x of every colum 

change the y as you want
```  python
y = 700
``` 

than change the if statments to check for your coordinates

```python
if ag.pixel(876, y)[0] == 0:
        click(876, y)
```

## What to take away from this

It is very simple today to perform such tasks, perhaps you've learned how you could this,
or perhaps yoy have understood that this isn't really such art, either way I felt the need to publish something like this. 
