import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

#class apresentation:
    #def __init__(self, master):
        #self.master = master
        #self.master.title("App Name")
        #self.name.geometry("350x200")
        #self.master.resizable(0, 0)

        #self.button_sign_up = tk.Button(self.master, text = "Sign up", fg = "black", font = "arial", command= SignUp)
        #self.button_sign_up.grid(row=3, column=1)

        
        #self.button_Login = tk.Button(self.master, text = "Sign up", fg = "black", font = "arial", command= Login)
        #self.button_Login.grid(row=4, column=1)

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
        self.button_sign_up.grid(row=3, column=1, pady=5)

        self.button_open_login = tk.Button(self.master, text='Login', command=self.open_login_window)
        self.button_open_login.grid(row=4, column=0, pady=5)

        self.button_open_server = tk.Button(self.master, text='Server', command=self.open_server_window)
        self.button_open_server.grid(row=4, column=1, pady=5)

    def store_user_data(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username and password:
            if username not in self.user_data:
                self.user_data[username] = password
                print("User Data Stored:", self.user_data)
                self.entry_username.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
                messagebox.showinfo("Success", "User registered successfully!")
            else:
                messagebox.showwarning("Input Error", "Username already exists!")
        else:
            messagebox.showwarning("Input Error", "Please enter both username and password")
        
    def open_login_window(self):
        login_window = tk.Toplevel(self.master)
        Login(login_window, self)

    def open_server_window(self):
        server_window = tk.Toplevel(self.master)
        ServerManager(server_window)


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
        self.button_login.grid(row=3, column=1, pady=5)

        self.button_close = tk.Button(self.master, text='Close', command=self.close_app)
        self.button_close.grid(column=0, row=4, pady=5)
    
    def close_app(self):
        self.master.destroy()

    def check_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in self.sign_up_instance.user_data and self.sign_up_instance.user_data[username] == password:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")


class ServerManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Server Manager")
        self.master.geometry("500x300")
        self.master.resizable(0, 0)

        # Sample server data
        self.servers = [
            {"Type": "Database", "Description": "Main DB server", "Name": "DB_Server_1"},
            {"Type": "Web", "Description": "Main web server", "Name": "Web_Server_1"}
        ]

        # Create the Treeview widget for displaying server information
        self.tree = ttk.Treeview(self.master, columns=("Type", "Description", "Name"), show='headings')
        self.tree.heading("Type", text="Type")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Name", text="Name")
        self.tree.pack(expand=True, fill='both')

        # Populate the table with data
        self.update_table()

        # Buttons for adding and editing server information
        self.button_add_server = tk.Button(self.master, text='Add Server', command=self.add_server)
        self.button_add_server.pack(side=tk.LEFT, padx=5, pady=5)

        self.button_edit_server = tk.Button(self.master, text='Edit Server', command=self.edit_server)
        self.button_edit_server.pack(side=tk.LEFT, padx=5, pady=5)

        self.button_close = tk.Button(self.master, text='Close', command=self.master.destroy)
        self.button_close.pack(side=tk.LEFT, padx=5, pady=5)

    def update_table(self):
        # Clear existing rows
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Insert new data
        for server in self.servers:
            self.tree.insert("", tk.END, values=(server["Type"], server["Description"], server["Name"]))

    def add_server(self):
        server_data = self.get_server_data()
        if server_data:
            self.servers.append(server_data)
            self.update_table()

    def edit_server(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, 'values')
            server_data = self.get_server_data(item_values)
            if server_data:
                for server in self.servers:
                    if server["Name"] == item_values[2]:
                        server.update(server_data)
                        break
                self.update_table()

    def get_server_data(self, existing_data=None):
        type_ = simpledialog.askstring("Server Type", "Enter the server type:", initialvalue=existing_data[0] if existing_data else "")
        description = simpledialog.askstring("Server Description", "Enter the server description:", initialvalue=existing_data[1] if existing_data else "")
        name = simpledialog.askstring("Server Name", "Enter the server name:", initialvalue=existing_data[2] if existing_data else "")
        if type_ and description and name:
            return {"Type": type_, "Description": description, "Name": name}
        else:
            messagebox.showwarning("Input Error", "All fields are required")
            return None


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x150")

    sign_up_instance = SignUp(root)

    button_login = tk.Button(root, text="Login", command=sign_up_instance.open_login_window)
    button_login.pack(pady=5)

    button_server = tk.Button(root, text="Server", command=sign_up_instance.open_server_window)
    button_server.pack(pady=5)

    root.mainloop()
