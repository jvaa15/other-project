import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk 

class TableWindow:
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

