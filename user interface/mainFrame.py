import tkinter as tk
from headerFrame import headerFrame
from contentFrame import contentFrame
from footerFrame import footerFrame

class mainFrame:
    def __init__(self, window):
        self.window = window
        self.main_frame = tk.Frame(
            self.window,
            bg="#FFC0CB"
        )
        self.main_frame.place(
            relwidth=0.9,
            relheight=0.8,
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        self.main_frame.config(
            highlightthickness=5,
            highlightbackground="#673147",
            highlightcolor="#673147"
        )
        self.header_frame = headerFrame(self.main_frame)
        self.content_frame = contentFrame(self.main_frame)
        self.footer_frame = footerFrame(self.main_frame)
