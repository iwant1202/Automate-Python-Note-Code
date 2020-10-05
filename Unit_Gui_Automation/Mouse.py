import pyautogui
#If mouse at 0,0 before executing a move mouse function, raise exception
#1/10 second pause between each call
#pyautogui.displayMousePosition() run in CMD, can be used to find app locations
#Gives coordinates and RGB
#pyautogui.readthedocs.org

#Treat computer as cartesian plane
#0,0 is top-left, x increasing to right, y increasing going down

print(pyautogui.size())
#returns resolution, int list

width, height = pyautogui.size()
#multiple assignment trick

print(width)
print(height)

print(pyautogui.position())
#Returns mouse position, int list

pyautogui.moveTo(10,10)
#Moves mouse to coordinates

pyautogui.moveTo(500, 500, duration=1.5)
#moves mouse to position in 1.5seconds

pyautogui.moveRel(200, 0)
pyautogui.moveRel(200, 0, duration = 2)
#Moves mouse 200 pixels to the right
#Relative of current position
pyautogui.moveRel(0, -100, duration=1)
#Moves mouse up 100 pixels

pyautogui.click(1354, 58)
#Clicks at the location listed
#Instantly moves, then clicks
#Lots of other options
pyautogui.rightClick(1354, 58)
pyautogui.doubleClick(1354, 58)
pyautogui.middleClick(1354, 58)
pyautogui.click()
#clicks where the mouse currently is
