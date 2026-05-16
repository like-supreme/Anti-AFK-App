🖱️ Anti AFK App
A lightweight Python desktop application that automatically moves your mouse to prevent AFK (Away From Keyboard) detection. Built with Tkinter for the UI and pyautogui for mouse control, it runs silently in the background with optional click and scroll support.

✨ Features

Automatic mouse movement — Moves the mouse in a square pattern at a set interval
Optional mouse click — Toggle on/off via checkbox before or during a session
Optional scroll — Toggle horizontal and vertical scroll on/off independently
Start / Stop control — Background thread starts and stops instantly without freezing the UI
Visual feedback — Start button turns green when active, Stop button turns red when inactive
One-click launch — .bat file handles missing dependencies automatically on first run


📁 Project Structure
mouse_mover/
├── main.py                  # Entry point — initializes Tkinter window
├── run.bat                  # One-click launcher with auto dependency install
├── src/
│   ├── __init__.py          # Marks src/ as a Python package
│   ├── ui.py                # Tkinter UI — layout, buttons, thread management
│   └── mouse_controller.py  # pyautogui wrapper — move, click, scroll logic

🛠️ Installation & Usage
Requirements: Python 3.x
Option 1 — Manual
bashpip install pyautogui
python main.py
Option 2 — One click
Double-click run.bat. If pyautogui is not installed, it will be installed automatically before launching the app.

🧠 What We Learned
Python & OOP

Structuring a project with multiple classes across separate files
Separating concerns: MouseController handles all mouse logic, MouseMoverUI handles all UI logic — neither bleeds into the other
Using relative imports (from .mouse_controller import ...) inside a package
Avoiding circular imports — importing only what you actually need in each file

Tkinter

Building layouts with grid() — managing rows, columns, padding, and sticky alignment
Working with widgets: Button, Checkbutton, Label, Entry
Using BooleanVar to track checkbox state and read it at runtime
Dynamically updating widget appearance with .config(bg=..., fg=...) based on app state
Properly destroying the window with root.destroy() and cleaning up background threads on exit

Threading

Running a loop in a background thread with threading.Thread so the UI stays responsive
Using daemon=True so the thread automatically exits when the main window closes
Controlling a thread with a _running boolean flag — the safe way to stop a thread without force-killing it
Guarding against double-starts by checking if self._running: return before spawning a new thread

pyautogui

Using move() for relative mouse movement vs moveTo() for absolute positioning
Adding duration to make mouse movement smooth and visible instead of instant
Scrolling vertically with scroll() and horizontally with hscroll()
Understanding why parameters should actually be used instead of ignored (the x, y bug)

Project Setup & Tooling

Writing a .bat launcher that checks for missing packages with pip show before running the app
Using if __name__ == "__main__" to prevent code from running on import
Structuring a project with a src/ folder and __init__.py for clean package management


🔧 Possible Improvements

 Let the user configure the movement interval (seconds) from the UI
 Add a system tray icon so the app can run minimized
 Show live mouse position (x, y) in the UI
 Add a launch-on-startup toggle
 Package the app as a standalone .exe with PyInstaller