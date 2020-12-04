# pyautogui helps us to type things and click on things on screen
# time is used for giving us time to enter into whatsapp web before starting to run the program
# and start spamming people
import pyautogui
import time
time.sleep(7)
with open("script.txt", mode="r") as file:
    for word in file:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(2)
