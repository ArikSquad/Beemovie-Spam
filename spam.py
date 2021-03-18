
import pyautogui
import time

time.sleep(3)
f = open("txt", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(1)
    
