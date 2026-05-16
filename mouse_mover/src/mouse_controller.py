import pyautogui
class MouseController:
    def __init__(self):
        self.x = 10 
        self.y = 10

    def move_mouse(self):
        pyautogui.move(50, 0, duration=0.3)
        pyautogui.move(0, 50, duration=0.3)
        pyautogui.move(-50, 0, duration=0.3)
        pyautogui.move(0, -50, duration=0.3)

    def click_mouse(self):
        pyautogui.click()

    def scroll_mouse(self, x, y):
        pyautogui.scroll(y)
        pyautogui.hscroll(x)
        return x,y

    def get_mouse_position(self):
        x, y = pyautogui.position()
        return x, y

    def get_monitor_size(self):
        x,y = pyautogui.size()   
        return x,y
    

