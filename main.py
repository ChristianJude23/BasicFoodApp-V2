import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.font import BOLD

#Color Palette: https://colorhunt.co/palette/b3c8cfbed7dcf1eedce5ddc5

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Food App")
        self.geometry("500x400")
        self.resizable(False, False)
        self.config(bg="#B3C8CF")

        self.create_login_widgets()

    def create_login_widgets(self):
        self.columnconfigure((1, 2, 3), weight=2)
        self.columnconfigure((0, 4), weight=1)
        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure(1, weight=10)
        
        lbl_title = tk.Label(self, text="Basic Food App", font=("Arial", 18, BOLD), bg="#B3C8CF")
        lbl_title.grid(row=0, column=0, columnspan=5, sticky='n', pady=10)

        frame = tk.Frame(self, bg="white", bd=3, relief=tk.GROOVE)
        frame.grid(row=1, column=1, columnspan=3, sticky="nsew")

        lbl_login = tk.Label(frame, text="Login", font=("Arial", 18), bg="white")
        lbl_usesrname = tk.Label(frame, text="Username:", font=("Arial", 16), bg="white")
        lbl_password = tk.Label(frame, text="Password:", font=("Arial", 16), bg="white")

        lbl_login.place(x=150, y=20)
        lbl_usesrname.place(x=20, y=80)
        lbl_password.place(x=20, y=120)

        ent_username = tk.Entry(frame, width=18, font=("Arial", 16), bd=3, relief=tk.GROOVE)
        ent_password = tk.Entry(frame, width=18, font=("Arial", 16), bd=3, relief=tk.GROOVE)

        ent_username.place(x=130, y=80)
        ent_password.place(x=130, y=120)

        btn_enter = tk.Button(frame, text="Enter", font=("Arial", 16), bg="#BED7DC", width=10)
        btn_enter.place(x=120, y=190)

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("")

app = Login()
app.mainloop()
