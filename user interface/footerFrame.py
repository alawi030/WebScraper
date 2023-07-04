import tkinter as tk

class footerFrame:
    def __init__(self, main_frame):
        self.main_frame = main_frame
        self.footer_frame = tk.Frame(
            self.main_frame,
            bg="#FFC0CB"
        )
        self.widgets()
    def widgets(self):
        self.frame()
        self.footer()
    def frame(self):
        self.footer_frame.place(
            relwidth=0.9,
            relheight=0.1,
            relx=0.5,
            rely=0.95,
            anchor="center"
        )
        self.footer_frame.config(
            highlightthickness=5,
            highlightbackground="#673147",
            highlightcolor="#673147"
        )
    def footer(self):
        self.footer_label = tk.Label(
            self.footer_frame,
            text="Footer",
            font=("Helvetica", 24),
            bg="#FFC0CB",
            fg="#F89880"
        )
        self.footer_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )