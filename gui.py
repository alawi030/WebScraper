import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Web Scraper")
        self.window.geometry("800x600")
        self.window.config(bg="#F89880")
        self.window.resizable(True, True)
        self.create_frames()
        self.place_frames()

    def create_frames(self):
        self.main_frame()
        self.title_frame()
        self.button_frame()
        self.content_frame()
        self.acknowledgments_frame()


    def place_frames(self):
        self.place_main_frame_widgets()
        self.place_title_frame_widgets()
        self.place_button_frame_widgets()
        self.place_acknowledgments_frame_widgets()
        

    def main_frame(self):
        self.main_frame = tk.Frame(
            self.window,
            bg="#FFC0CB"
        )
        
    def acknowledgments_frame(self):
        self.acknowledgments_frame = tk.Frame(
            self.main_frame,
            bg="#FFC0CB"
        )
        self.acknowledgments_label = tk.Label(
            self.acknowledgments_frame,
            text="A project by: Ali Almaliki.",
            font=("Helvetica", 14),
            bg="#FFC0CB",
            fg="#F89880"
        )
    
    def place_acknowledgments_frame_widgets(self):
        #at the bottom of the main frame
        self.acknowledgments_frame.place(
            relwidth=0.9,
            relheight=0.1,
            relx=0.5,
            rely=0.95,
            anchor="center"
        )
        self.acknowledgments_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

    def place_main_frame_widgets(self):
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

    def title_frame(self):
        self.title_frame = tk.Frame(
            self.main_frame,
            bg="#FFC0CB"
        )
        

        # logo is called appIcon.png inside the images folder
        self.logo = tk.PhotoImage(file="images/appIcon.png")
        self.logo_label = tk.Label(
            self.title_frame,
            image=self.logo,
            bg="#FFC0CB"
        )

        self.title_label = tk.Label(
            self.title_frame,
            text="Web Scraper",
            font=("Helvetica", 34),
            bg="#FFC0CB",
            fg="#673147"
        )

        self.title_line = tk.Label(
            self.main_frame,
            bg="#673147"
        )
        

    def place_title_frame_widgets(self):
        self.title_frame.place(
            relwidth=0.9,
            relheight=0.15,
            relx=0.5,
            rely=0.1,
            anchor="center"
        )

        self.logo_label.place(
            relx=0.15,
            rely=0.4,
            anchor="e"
        )

        self.title_label.place(
            relx=0.5,
            rely=0.4,
            anchor="center"
        )

        self.title_line.place(
            relwidth=0.9,
            relheight=0.005,
            relx=0.5,
            rely=0.15,
            anchor="center"
        )

    def button_frame(self):
        self.button_frame = tk.Frame(
            self.main_frame,
            bg="#FFC0CB"
        )

        button_names = ["News", "E-commerce", "Social Media", "Job Boards", "Weather", "Recipes"]
        self.buttons = []
        for i in range(6):
            if i < len(button_names):
                button = tk.Button(
                    self.button_frame,
                    text=button_names[i],
                    font=("Helvetica", 24),
                    bg="#FFC0CB",
                    fg="#673147",
                    relief="raised",
                    bd=1,
                    compound=tk.TOP
                )
                logo = tk.PhotoImage(file="images/" + button_names[i] + ".png")
                button.config(image=logo)
                button.image = logo

                button.grid(
                    row=i // 3,
                    column=i % 3,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

                button.config(command=lambda btn=button: self.button_click(btn))

                self.buttons.append(button)

        self.button_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.button_frame.grid_rowconfigure((0, 1, 2), weight=1)



    def place_button_frame_widgets(self):
        self.button_frame.place(
            relwidth=0.9,
            relheight=0.6,
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

    def button_click(self, button):
        self.title_label.config(text=button["text"])
        self.logo = tk.PhotoImage(file="images/" + button["text"] + ".png")
        self.logo_label.config(image=self.logo)
        self.button_frame.place_forget()
        self.acknowledgments_frame.place_forget()
        self.place_content_frame()

    def back_click(self):
        self.title_label.config(text="Web Scraper")
        self.logo = tk.PhotoImage(file="images/appIcon.png")
        self.place_acknowledgments_frame_widgets()
        self.logo_label.config(image=self.logo)
        self.content_frame.place_forget()
        self.place_button_frame_widgets()

    def content_frame(self):
        self.content_frame = tk.Frame(
            self.main_frame,
            bg="#FFC0CB"
        )
        

        self.back_button = tk.Button(
            self.content_frame,
            text="Back",
            font=("Helvetica", 20),
            bg="#FFC0CB",
            fg="#673147",
            relief="raised",
            height=1,
            width=10,
            bd=1,
            command=self.back_click
        )

    def place_content_frame(self):
            self.content_frame.place(
                relwidth=0.9,
                relheight=0.8,
                relx=0.5,
                rely=0.6,
                anchor="center"
            )
            
            self.back_button.place(
                relx=0,
                rely=0.95,
                anchor="sw"
            )


        # search bar with the placeholder "Search for something..."

        # search button

        # label : desired output format
        
        # radio buttons : csv, text, xml

if __name__ == "__main__":
    gui = GUI()
    gui.window.mainloop()
