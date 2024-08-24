
import tkinter as tk
from tkinter import messagebox, simpledialog


class SignUp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sign Up Window")
        self.master.geometry("350x200")
        self.master.resizable(0, 0)

        self.user_data = {}

        # Interface elements
        self.label_title = tk.Label(self.master, text='Sign Up', font='arial')
        self.label_title.grid(row=0, column=1)

        self.label_username = tk.Label(self.master, text='Username', font='arial')
        self.label_username.grid(row=1, column=0, pady=5)

        self.label_password = tk.Label(self.master, text='Password', font='arial')
        self.label_password.grid(row=2, column=0, pady=5)
        
        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=1, column=1)

        self.entry_password = tk.Entry(self.master, show='*')
        self.entry_password.grid(row=2, column=1)

        self.button_sign_up = tk.Button(self.master, text='Sign Up', command=self.store_user_data)
        self.button_sign_up.grid(row=3, column=1)

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
            messagebox.showwarning("Input Error", "Please enter both username and password")
        
    def open_login_window(self):
        login_window = tk.Toplevel(self.master)
        Login(login_window, self)

    def open_server_window(self):
        server_window = tk.Toplevel(self.master)
        Server(server_window)


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
    
    def close_app(self):
        self.master.destroy()

    def check_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in self.sign_up_instance.user_data and self.sign_up_instance.user_data[username] == password:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")


class Server:
    def __init__(self, master):
        self.master = master
        self.master.title("Server")
        self.master.geometry("350x200")
        self.master.resizable(0, 0)

        server = {}

        server_name = simpledialog.askstring("Server Name", "Enter the server name:")
        if server_name:
            self.label_title = tk.Label(self.master, text=server_name, fg='blue', font='arial')
            self.label_title.grid(row=0, column=1)
        else:
            messagebox.showwarning("No Name", "Server name cannot be empty")
            self.master.destroy()

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

    def close_app(self):
        self.master.destroy()

    def check_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # This should be adapted based on your server data handling
        # For now, this example assumes checking against a fixed username/password
        if username == "admin" and password == "password":
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x150")

    sign_up_instance = SignUp(root)

    button_login = tk.Button(root, text="Login", command=sign_up_instance.open_login_window)
    button_login.pack(pady=5)

    button_server = tk.Button(root, text="Open Server", command=sign_up_instance.open_server_window)
    button_server.pack(pady=5)

    root.mainloop()
