import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk    

class Login:
    def __init__(self, master, sign_up_instance):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry("350x200")
        self.master.resizable(0, 0)

        self.sign_up_instance = sign_up_instance
        
        # Interface elements
        self.label_title = tk.Label(self.master, text='Login', fg='blue', font='arial')
        self.label_title.grid(row=0, column=1)
        
        self.label_username = tk.Label(self.master, text='Username', font='arial')
        self.label_username.grid(row=1, column=0, pady=5)

        self.label_password = tk.Label(self.master, text='Password', font='arial')
        self.label_password.grid(row=2, column=0, pady=5)
        
        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=1, column=1)

        self.entry_password = tk.Entry(self.master, show='*')
        self.entry_password.grid(row=2, column=1)

        self.button_login = tk.Button(self.master, text='Login', command=self.check_login)
        self.button_login.grid(row=3, column=1)

        self.button_close = tk.Button(self.master, text='Close', command=self.close_app)
        self.button_close.grid(column=0, row=4)
     
    # Functions
    def close_app(self):
        self.master.destroy()

    def check_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in self.sign_up_instance.user_data and self.sign_up_instance.user_data[username] == password:
            messagebox.showinfo("Success", "Login successful!")
            self.master.destroy()
            
        else:
            messagebox.showerror("Error", "Invalid username or password")

