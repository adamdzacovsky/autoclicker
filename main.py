import pyautogui
import time
import tkinter
from tkinter import messagebox
import keyboard

start_clicking_button = "s"
end_clicking_button = "e"
end_program = "d"
is_running = True
is_clicking = False
click_x = 0
click_y = 0

box = tkinter.Tk()
box.withdraw()

print("Spustila sa aplikacia AC")

def moj_click(x, y):
    print(f"Klik x = {x}, y = {y}")
    #pyautogui.click(x,y)

while is_running:
    if keyboard.is_pressed(start_clicking_button):
        is_clicking = True
        print("Klikanie spustene")
        print("Daj kurzor na miesto")
        time.sleep(1)
     #   click_x,click_y = pyautogui.position()
    elif keyboard.is_pressed(end_clicking_button):
        is_clicking = False
        print("Klikanie zastavene")
        time.sleep(0.5)
    elif keyboard.is_pressed(end_program):
        is_running = False
        messagebox.showinfo("program skonceny", "uspesne ukonceny program")
        print("Program skonceny")
        time.sleep(0.5)
    while is_clicking:
        click_x,click_y = pyautogui.position()
        moj_click(click_x, click_y)
        if keyboard.is_pressed(end_clicking_button):
            is_clicking = False
            print("Klikanie zastavene po spusteni")