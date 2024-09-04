import tkinter as tk

class SignUp:
    def __init__(self, master):
        self.master = master

    def open_login_window(self):
        login_window = tk.Toplevel(self.master)
        login_window.title("Login Window")
        login_window.geometry("300x150")

    def open_server_window(self):
        server_window = tk.Toplevel(self.master)
        server_window.title("Server Window")
        server_window.geometry("300x150")

# Testando a janela principal
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x150")
    
    # Instância da classe SignUp
    sign_up_instance = SignUp(root)
    
    # Botão para abrir janela de login
    button_login = tk.Button(root, text="Login", command=sign_up_instance.open_login_window)
    button_login.pack(pady=5)

    # Botão para abrir janela de servidor
    button_server = tk.Button(root, text="Server", command=sign_up_instance.open_server_window)
    button_server.pack(pady=5)

    # Iniciando o loop principal
    root.mainloop()
