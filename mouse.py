import pyautogui
import random

screenWidth, screenHeight = pyautogui.size()
for i in range(200):
    w = random.randint(200, screenWidth-200)
    h = random.randint(200, screenHeight-200)
    pyautogui.moveTo(w, h, duration=0.1)