import tkinter as tk

class contentFrame:
    def __init__(self, main_frame):
        self.main_frame = main_frame
        self.content_frame = tk.Frame(
            self.main_frame,
            bg="#FFC0CB"
        )
        self.content_frame.place(
            relwidth=0.9,
            relheight=0.6,
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        self.title = tk.Label(
            self.content_frame,
            text="What would you like to scrape?",
            font=("Helvetica", 24),
            bg="#FFC0CB",
            fg="#673147"
        )
        self.title.place(
            relx=0.5,
            rely=0.1,
            anchor="center"
        )
        self.line = tk.Label(
            self.content_frame,
            bg="#673147"
        )
        self.line.place(
            relwidth=0.9,
            relheight=0.005,
            relx=0.5,
            rely=0.2,
            anchor="center"
        )
        self.buttons = []
        self.button_names = ["News", "E-commerce", "Social Media", "Job Boards", "Weather", "Recipes"]
        # 2x3 grid
        for i in range(6):
            if i < len(self.button_names):
                button = tk.Button(
                    self.content_frame,
                    text=self.button_names[i],
                    font=("Helvetica", 24),
                    bg="#FFC0CB",
                    fg="#673147",
                    command=lambda i=i: self.button_command(i)
                )
                button.grid(
                    row=i // 3,
                    column=i % 3,
                    padx=1,
                    pady=1
                )
                self.buttons.append(button)

                # make the buttons closer together
                self.content_frame.grid_columnconfigure(i % 3, weight=1)
                self.content_frame.grid_rowconfigure(i // 3, weight=1)

                # make the buttons same size
                self.content_frame.grid_columnconfigure((0, 1, 2), uniform="uniform")

