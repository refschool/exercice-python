import pyautogui
import time

for line in open("source.txt", "r"):
    time.sleep(2)
    pyautogui.typewrite(line)

    pyautogui.press("enter")