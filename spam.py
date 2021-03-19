
import pyautogui
import time

time.sleep(3)
f = open("txt", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(1)
    # we want to use time.sleep(1) because some apps doesnt allow spamming so this will bypass
    
