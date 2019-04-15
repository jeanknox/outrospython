import pyautogui
import time
image = "button.png"
while True:
	image_local = pyautogui.locateOnScreen(image)
	image_local = pyautogui.center(image_local)
	pyautogui.moveTo(image_local)
	time.sleep(5)
