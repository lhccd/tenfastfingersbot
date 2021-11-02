import pyautogui, time

while(True):
    pyautogui.moveTo(0,0)
    pyautogui.click()
    print("Cursor moved, you're online")
    time.sleep(30)
