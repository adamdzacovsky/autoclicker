import pyautogui
import time
import keyboard


class AutoClicker:
    def __init__(self, start_key = "s", stop_key = "e", exit_key = "d", delay = 0.1):
        self.start_key = start_key
        self.stop_key = stop_key
        self.exit_key = exit_key
        self.delay = delay

        self.is_clicking = False
        self.is_running = True
        self.click_x = 0
        self.click_y = 0

        print("Autoclicker has started")

    def click(self, x, y):
        print(f"Click x = {x}, y = {y}")
        #pyautogui.click(x,y)        

    def start(self):
        while self.is_running:
            if keyboard.is_pressed(self.start_key):
                self.is_clicking = True
                print("Clicking has started")
                time.sleep(1)
            elif keyboard.is_pressed(self.stop_key):
                self.is_clicking = False
                print("Clicking has ended")
                time.sleep(1)
            elif keyboard.is_pressed(self.exit_key):
                self.is_running = False
                print("Autoclicker has ended")
            
            while self.is_clicking:
                self.click_x, self.click_y = pyautogui.position()
                self.click(self.click_x, self.click_y)

                if keyboard.is_pressed(self.stop_key):
                    self.is_clicking = False
                