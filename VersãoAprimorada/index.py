import tkinter as tk
from auth.sign_up import SignUp
from auth.login import Login
from window.table_window import TableWindow

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
