import tkinter as tk
from tkinter import ttk, messagebox
from credenciais import salvar_credenciais, carregar_credenciais
from automacao import login_sigaa

class AppSIGAA:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Automático no SIGAA")
        self.root.geometry("420x300")
        self.root.configure(bg="#f5f9ff")

        self.criar_interface()

    def criar_interface(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TLabel", background="#f5f9ff", foreground="#1a237e", font=("Segoe UI", 11))
        style.configure("TEntry", fieldbackground="#ffffff", foreground="#000000", padding=5)
        style.configure("TButton", font=("Segoe UI", 10, "bold"), background="#2196f3", foreground="white", padding=6)
        style.map("TButton", background=[("active", "#1976d2")])

        ttk.Label(self.root, text="Login Automático no SIGAA", font=("Segoe UI", 15, "bold")).pack(pady=15)

        frame = tk.Frame(self.root, bg="#f5f9ff")
        frame.pack(pady=10)

        ttk.Label(frame, text="ID SIGAA:").grid(row=0, column=0, sticky="e", pady=5, padx=10)
        self.inputID_sigaa = ttk.Entry(frame, width=30)
        self.inputID_sigaa.grid(row=0, column=1, pady=5, padx=10)

        ttk.Label(frame, text="Senha SIGAA:").grid(row=1, column=0, sticky="e", pady=5, padx=10)
        self.inputSenha_sigaa = ttk.Entry(frame, show="*", width=30)
        self.inputSenha_sigaa.grid(row=1, column=1, pady=5, padx=10)

        ttk.Button(self.root, text="Salvar Informações", command=self.salvar_info).pack(pady=6)
        ttk.Button(self.root, text="Executar Login", command=self.automacao).pack()

    def limpar_formulario(self):
        self.inputID_sigaa.delete(0, tk.END)
        self.inputSenha_sigaa.delete(0, tk.END)

    def salvar_info(self):
        sigaa_id = self.inputID_sigaa.get().strip()
        sigaa_senha = self.inputSenha_sigaa.get().strip()
        if not sigaa_id or not sigaa_senha:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        salvar_credenciais(sigaa_id, sigaa_senha)
        messagebox.showinfo("Sucesso", "Informações salvas com sucesso!")
        self.limpar_formulario()

    def automacao(self):
        credenciais = carregar_credenciais()
        if not credenciais:
            messagebox.showerror("Erro", "Nenhuma informação salva!")
            return

        usuario, senha = credenciais
        resultado = login_sigaa(usuario, senha)

        if "sucesso" in resultado.lower():
            messagebox.showinfo("Sucesso", resultado)
        else:
            messagebox.showerror("Erro", resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppSIGAA(root)
    root.mainloop()
