import tkinter as tk
from mainFrame import mainFrame

class window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Web Scraper")
        self.window.geometry("800x700")
        self.window.config(bg="#F89880")
        self.window.resizable(True, True)
        self.main_frame = mainFrame(self.window)

if __name__ == "__main__":
    window = window()
    window.window.mainloop()
