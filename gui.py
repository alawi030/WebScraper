import tkinter as tk
from PIL import Image, ImageTk

class WebScraper:
    def __init__(self, root):
        self.root = root
        self.root.title("WebScraper")
        self.root.geometry("800x700")
        self.root.config(bg="#F4E3CB")

        self.frame = MainFrame(self.root)
        self.footer_frame = FooterFrame(self.root)

class MainFrame:
    def __init__(self, root):
        self.frame = tk.Frame(root, bg="#FFE8D6", bd=10, relief=tk.RAISED)
        self.frame.place(relx=0.5, rely=0.5, relwidth=0.85, relheight=0.8, anchor=tk.CENTER)

        self.header_frame = HeaderFrame(self.frame)
        self.content_frame = ContentFrame(self.frame)

class HeaderFrame:
    def __init__(self, root):
        self.header_frame = tk.Frame(root, bg="#FFE8D6", bd=1, relief=tk.RAISED)
        self.header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.15, anchor=tk.NW)

        self.create_header()

    def create_header(self):
        label_text = tk.Label(self.header_frame, text="Web Scraper", font=("Arial", 28, "bold"), bg="#FFE8D6", fg="#C47804")
        label_text.pack(pady=10)

class ContentFrame:
    def __init__(self, root):
        self.content_frame = tk.Frame(root, bg="#FFE8D6", bd=2, relief=tk.RAISED)
        self.content_frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.85, anchor=tk.NW)

        self.create_content()

    def create_content(self):
        label = tk.Label(self.content_frame, text="What would you like to scrape?", font=("Arial", 22), bg="#FFE8D6", fg="#C47804")
        label.pack(pady=(20, 10))

        button_names = ["News", "E-commerce", "Social Media", "Job Boards", "Weather", "Recipes"]

        buttons_frame = tk.Frame(self.content_frame, bg="#FFE8D6")
        buttons_frame.pack(pady=(0, 20))

        for i in range(2):
            buttons_frame.grid_rowconfigure(i, weight=1)
            for j in range(3):
                buttons_frame.grid_columnconfigure(j, weight=1)

                button = tk.Button(buttons_frame, text=button_names[i*3 + j], width=15, height=5,
                                font=("Arial", 18), fg="#C47804", padx=10, pady=10)
                button.grid(row=i, column=j, padx=10, pady=10)

class FooterFrame:
    def __init__(self, root):
        self.footer_frame = tk.Frame(root, bg="#F4E3CB")
        self.footer_frame.place(relx=0, rely=1, relwidth=1, anchor=tk.SW)

        self.create_footer()

    def create_footer(self):
        label = tk.Label(self.footer_frame, text="A project by: Ali Almaliki.", font=("Arial", 12), bg="#F4E3CB", fg="#C47804")
        label.pack(pady=10)


root = tk.Tk()
app = WebScraper(root)
root.mainloop()