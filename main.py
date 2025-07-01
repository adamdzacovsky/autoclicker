import pyautogui
import time
import keyboard

start_clicking_button = "s"
end_clicking_button = "e"
end_program = "d"
is_running = True
is_clicking = False
print("Spustila sa aplikacia AC")
while is_running:
    if keyboard.is_pressed(start_clicking_button):
        is_clicking = True
        print("Klikanie spustene")
        time.sleep(0.5)
    elif keyboard.is_pressed(end_clicking_button):
        is_clicking = False
        print("Klikanie zastavene")
        time.sleep(0.5)
    elif keyboard.is_pressed(end_program):
        is_running = False
        print("Program skonceny")
        time.sleep(0.5)
    while is_clicking:
        print("Klik")
        pyautogui.click()
        if keyboard.is_pressed(end_clicking_button):
            is_clicking = False
            print("Klikanie zastavene po spusteni")

        