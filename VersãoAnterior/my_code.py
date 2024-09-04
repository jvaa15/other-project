import tkinter as tk
from tkinter import messagebox


# problems:
# 1 ain´t no opening the button of login, sign up.
# 2 the txt in the main window ain´t no poping up.
# #


ctrl = 0


class MainWindow:
    def __init__(self, master):

        # definitions from the main window

        self.master = master
        self.master.title("Main Window")
        self.master.geometry("350x200")
        self.master.resizable(0, 0)

        # Interface elements main window
        self.h1 = tk.Text("hello, welcome to the app!\n Login or Sign up?")
        self.h1.grid(row=1, column=1)  # i rly hope this is gonna work!
        # Sign up button
        self.SignUp_button = tk.Button(
            self.master, text="Sign Up", command=SignUp())
        self.SignUp_button.grid(row=3, column=2)
        # login button
        self.Login_button = tk.Button(
            self.master, text="Login", command=Login())
        self.Login_button.grid(row=4, column=3)

        if ctrl == 1:
            btn_change()


def btn_change():
    global ctrl
    ctrl += 1


class SignUp:
    def __init__(self, master):
        # Interface elements sign up
        self.master = master
        self.master.title("Sign Up Window")
        self.master.geometry("350x200")
        self.master.resizable(0, 0)

        # Dictionary to store the variables from the sign up
        self.user_data = {}

        # Interface elements sign up
        self.label_title = tk.Label(self.master, text='Sign Up', font='arial')
        self.label_title.grid(row=0, column=1)

        self.label_username = tk.Label(
            self.master, text='Username', font='arial')
        self.label_username.grid(row=1, column=0, pady=5)

        self.label_password = tk.Label(
            self.master, text='Password', font='arial')
        self.label_password.grid(row=2, column=0, pady=5)

        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=1, column=1)

        self.entry_password = tk.Entry(self.master, show='*')
        self.entry_password.grid(row=2, column=1)

        self.button_sign_up = tk.Button(
            self.master, text='Sign Up', command=self.store_user_data)
        self.button_sign_up.grid(row=3, column=1)

    # Functions from sign up

    def store_user_data(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username and password:
            self.user_data[username] = password
            print("User Data Stored:", self.user_data)
            self.entry_username.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            messagebox.showinfo("Success", "User registered successfully!")
        else:
            messagebox.showwarning(
                "Input Error", "Please enter both username and password")


class Login:
    def __init__(self, master):
        # Interface elements Login
        self.master = master
        self.master.title("Login Window")
        self.master.geometry("350x200")
        self.master.resizable(0, 0)

        self.sign_up_instance = sign_up_instance

        # Interface elements from the login

        self.label_title = tk.Label(
            self.master, text='Login', fg='blue', font='arial')
        self.label_title.grid(row=0, column=1)

        self.label_username = tk.Label(
            self.master, text='Username', font='arial')
        self.label_username.grid(row=1, column=0, pady=5)

        self.label_password = tk.Label(
            self.master, text='Password', font='arial')
        self.label_password.grid(row=2, column=0, pady=5)

        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=1, column=1)

        self.entry_password = tk.Entry(self.master, show='*')
        self.entry_password.grid(row=2, column=1)

        self.button_login = tk.Button(
            self.master, text='Login', command=self.check_login)
        self.button_login.grid(row=3, column=1)

        self.button_close = tk.Button(
            self.master, text='Close', command=self.close_app)
        self.button_close.grid(column=0, row=4)

    # Functions from the login

    def close_app(self):
        self.master.destroy()

    def check_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in self.sign_up_instance.user_data and self.sign_up_instance.user_data[username] == password:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")



if __name__ == '__main__':

    root_MainWindow = tk.Tk()
    root_MainWindow.mainloop()

    if ctrl == 1:

        root_sign_up = tk.Tk()
        root_login = tk.Tk()

        sign_up_instance = SignUp(root_sign_up)
        login_instance = Login(root_login, sign_up_instance)
        root_sign_up.mainloop()
        root_login.mainloop() # what´s wrong here???