
# area for the interface#

import tkinter as tk
from tkinter import messagebox as msg

class server():
    def __init__(self, master):

        self.master = master
        self.master.title("Server")
        self.master.geometry("200x200")
        self.master.resizable(0, 0)

        self.title = tk.Label(self.master, text = "App Server", font = "arial")
        self.title.grid(row = 0, column= 1)
        






# functions and "server area"
# #

user_data = {}

def entry_user(key, value):
    user_data[key] = value
    print(f"Stored Successfully: {key} -> {value}")

def Login(key):
    if key in user_data:
        print("logged Successfully!")
        return user_data[key]
    else:
        print("Wrong key")

def delete_entry(key):
    if key in user_data:
        del user_data[key]
        print("Deleted Successfully")
    else:
        print("Key not found!")

def new_entry(key, new_value):
    if key in user_data:
        user_data[key] = new_value
        print(" Key updated successfully! {key} -> {new_value}")
    else:
        print("key {key} not found")



# and the code from chat gpt#

# Initialize an empty dictionary
data_store = {}

def add_entry(key, value):
    """Add a new entry to the data store."""
    data_store[key] = value
    print(f"Entry added: {key} -> {value}")

def update_entry(key, new_value):
    """Update the value of an existing entry."""
    if key in data_store:
        data_store[key] = new_value
        print(f"Entry updated: {key} -> {new_value}")
    else:
        print(f"Key '{key}' not found. Use add_entry() to add it.")

def get_entry(key):
    """Retrieve the value of an entry."""
    return data_store.get(key, 'Key not found')

def delete_entry(key):
    """Delete an entry from the data store."""
    if key in data_store:
        del data_store[key]
        print(f"Entry deleted: {key}")
    else:
        print(f"Key '{key}' not found.")

# Example usage
if __name__ == "__main__":
    # Add entries
    add_entry('name', 'Alice')
    add_entry('age', 30)
    add_entry('city', 'New York')

    # Retrieve and print an entry
    print(f"Name: {get_entry('name')}")  # Output: Alice

    # Update an existing entry
    update_entry('age', 31)

    # Print the updated entry
    print(f"Updated Age: {get_entry('age')}")  # Output: 31

    # Delete an entry
    delete_entry('city')

    # Try to retrieve a deleted entry
    print(f"City: {get_entry('city')}")  # Output: Key not found





        
        
    
