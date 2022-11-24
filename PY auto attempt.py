import pyautogui
import time
import subprocess

time.sleep(0.5)

cmd = "cmd.exe"

pyautogui.hotkey("ctrl","esc")
pyautogui.PAUSE = 0.5
pyautogui.write("cmd")
pyautogui.PAUSE = 0.5
pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5
pyautogui.click(button='left', x=960, y=540)
pyautogui.PAUSE = 0.5
pyautogui.write("net user")
pyautogui.PAUSE = 0.5
pyautogui.hotkey("enter")


