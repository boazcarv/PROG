"""
Capítulo 6 - Interface Gráfica do Usuário (GUI) com Tkinter
Rode com:  python3 cap06_gui.py

Exemplo mínimo: um cadastro de contatos em memória, feito com POO
(a janela é uma CLASSE que herda de tk.Tk).
"""

import tkinter as tk
from tkinter import ttk, messagebox


class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class JanelaContatos(tk.Tk):        # HERANÇA: nossa janela É-UMA janela Tk
    def __init__(self):
        super().__init__()
        self.title("Agenda de Contatos")
        self.geometry("420x320")

        self.contatos: list[Contato] = []      # ESTADO da janela
        self._montar_widgets()                 # COMPORTAMENTO

    # ---------- construção da interface ----------
    def _montar_widgets(self):
        form = ttk.Frame(self, padding=10)
        form.pack(fill="x")

        ttk.Label(form, text="Nome:").grid(row=0, column=0, sticky="w")
        self.entrada_nome = ttk.Entry(form, width=30)
        self.entrada_nome.grid(row=0, column=1, padx=5, pady=3)

        ttk.Label(form, text="Telefone:").grid(row=1, column=0, sticky="w")
        self.entrada_tel = ttk.Entry(form, width=30)
        self.entrada_tel.grid(row=1, column=1, padx=5, pady=3)

        botoes = ttk.Frame(self, padding=(10, 0))
        botoes.pack(fill="x")
        # command= liga o BOTÃO a um MÉTODO do objeto
        ttk.Button(botoes, text="Adicionar",
                   command=self.adicionar).pack(side="left")
        ttk.Button(botoes, text="Remover selecionado",
                   command=self.remover).pack(side="left", padx=5)

        self.lista = tk.Listbox(self, height=10)
        self.lista.pack(fill="both", expand=True, padx=10, pady=10)

    # ---------- ações (handlers) ----------
    def adicionar(self):
        nome = self.entrada_nome.get().strip()
        tel = self.entrada_tel.get().strip()
        if not nome or not tel:
            messagebox.showwarning("Campos vazios",
                                   "Preencha nome e telefone.")
            return
        self.contatos.append(Contato(nome, tel))
        self.entrada_nome.delete(0, tk.END)
        self.entrada_tel.delete(0, tk.END)
        self.atualizar_lista()

    def remover(self):
        selecao = self.lista.curselection()
        if not selecao:
            messagebox.showinfo("Nada selecionado",
                                "Clique em um contato da lista.")
            return
        del self.contatos[selecao[0]]
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for c in self.contatos:
            self.lista.insert(tk.END, f"{c.nome} — {c.telefone}")


if __name__ == "__main__":
    JanelaContatos().mainloop()
