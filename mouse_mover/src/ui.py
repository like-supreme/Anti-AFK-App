from tkinter import *
from tkinter import messagebox
from .mouse_controller import MouseController as mc
import threading
import time
class MouseMoverUI:
    def __init__(self, master):
        self.mc = mc()
        self.root = master
        self.root.geometry("500x500")
        self.root.title("Anti AFK APP")

        self._running = False
        self._thread = None
        
        title_label = Label(self.root,
                            text="Anti AFK APP",
                            font=("Arial", 20, "bold"),
                            fg="white", bg="blue")
        title_label.grid(row=0, column=0, columnspan=3,sticky="ew")
        self.click_var = BooleanVar()  # ← eklendi
        self.inp_click_button = Checkbutton(self.root, text="Mouse click", variable=self.click_var, command=self.on_click_button_click)
        self.inp_click_button.grid(row=1, column=1, padx=10, pady=10)

        self.scroll_var = BooleanVar()  # ← eklendi
        inp_scroll_button = Checkbutton(self.root, text="Scroll olsun mu", variable=self.scroll_var, command=self.on_scroll_button_click)
        inp_scroll_button.grid(row=2, column=1, padx=10, pady=10)

        self.start_button = Button(self.root, text="Start", command=self.on_move_button_click)
        self.start_button.grid(row=3,column=0,padx=10,pady=10)

        self.stop_button = Button(self.root, text="Stop", command=self.stop_clicking)
        self.stop_button.grid(row=3,column=1,padx=10,pady=10)

        exit_button = Button(self.root, text="Exit", command=self.exit_click)
        exit_button.grid(row=3,column=2,padx=10,pady=10)  

    def move_loop(self):
        while self._running:
            self.mc.move_mouse()
            if self.click_var.get():
                self.mc.click_mouse()
            if self.scroll_var.get():
                self.mc.scroll_mouse(0, 0)
            time.sleep(1)

    def update_mouse_position(self, x, y):
        print(f"X={x}, Y={y}")

    def on_click_button_click(self):
        if self.click_var.get():
            print("Click aktif")
        else:
            print("Click deaktif")


    def on_move_button_click(self):
        if self._running:
            return  # zaten çalışıyorsa tekrar başlatma
        
        self._running = True
        self.start_button.config(bg="green", fg="white")
        self.stop_button.config(bg="SystemButtonFace", fg="black")  # stop default'a dön

        self._thread = threading.Thread(target=self.move_loop, daemon=True)
        self._thread.start()

    def on_scroll_button_click(self):
        if self.scroll_var.get():
            print("Scroll aktif")
        else:
            print("Scroll deaktif")

    def on_get_position_button_click(self):
        x, y = self.mc.get_mouse_position()
        self.update_mouse_position(x, y)
    
    def show_message(self, message):
        messagebox.showinfo("Bilgi",message)
    
    def stop_clicking(self):
        self._running = False
        self.stop_button.config(bg="red", fg="white")
        self.start_button.config(bg="SystemButtonFace", fg="black")

    def exit_click(self):
        self._running = False
        self.root.destroy()