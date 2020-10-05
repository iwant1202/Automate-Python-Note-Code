import pyautogui


pyautogui.click(321, 92); pyautogui.typewrite('Hello world!')
#semicolon allows two commands in one line
#Click on something, and then type into that field

pyautogui.typewrite('Hello world!', interval=0.2)
#Creates .2 second interval between typing

pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)
#Sends list, operates sequentially
#'left' means left arrow key

print(pyautogui.KEYBOARD_KEYS)
#equals a list of different usable keyboard keys

pyautogui.press('f1')
#presses f1 button

pyautogui.hotkey('ctrl', 'o')
#presses in order
