import tkinter as tk
class headerFrame:
    def __init__(self, main_frame):
        self.main_frame = main_frame
        self.header_frame = tk.Frame(
            self.main_frame,
            bg="#FFC0CB"
        )
        self.header_frame.place(
            relwidth=0.9,
            relheight=0.15,
            relx=0.5,
            rely=0.1,
            anchor="center"
        )
        self.widgets()

    def widgets(self):
        self.logo()
        self.title()
        self.line()

    def logo(self):
        self.logo = tk.PhotoImage(file="images/appIcon.png")
        self.logo_label = tk.Label(
            self.header_frame,
            image=self.logo,
            bg="#FFC0CB"
        )
        self.logo_label.place(
            relx=0.15,
            rely=0.4,
            anchor="e"
        )

    def title(self):
        self.title_label = tk.Label(
            self.header_frame,
            text="Web Scraper",
            font=("Helvetica", 34),
            bg="#FFC0CB",
            fg="#673147"
        )
        self.title_label.place(
            relx=0.5,
            rely=0.4,
            anchor="center"
        )

    def line(self):
        self.line = tk.Label(
            self.main_frame,
            bg="#673147"
        )
        self.line.place(
            relwidth=0.9,
            relheight=0.005,
            relx=0.5,
            rely=0.15,
            anchor="center"
        )

    