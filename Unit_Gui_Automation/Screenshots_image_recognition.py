import pyautogui

pyautogui.screenshot()
#Returns a pillow image object

pyautogui.screenshot(r'C:\Users\nicho\Desktop\PythonPrograms\TestFiles\'' +\
'screenshot_example.png')
#Saves a screenshot as file to location

chromeLoc = pyautogui.locateOnScreen(r'C:\Users\nicho\Desktop' +\
                         '\PythonPrograms\TestFiles\\Nlogo.png')
#Return int list: x location, y location, width, height
print(chromeLoc)

centerLoc = pyautogui.locateCenterOnScreen(r'C:\Users\nicho\Desktop' +\
                         '\PythonPrograms\TestFiles\\Nlogo.png')

#Returns x,y location of the center of the object
print(centerLoc)

#Locating functions very expensive
#Image matches must be pixel perfect

x,y = centerLoc
pyautogui.moveTo((x, y), duration=1)
pyautogui.click()
