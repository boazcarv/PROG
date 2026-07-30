"""Interface gráfica do sistema (Tópico 6)."""

import tkinter as tk
from tkinter import ttk, messagebox

from ..excecoes import ErroBiblioteca
from ..modelos import Livro, DVD
from ..servicos import Acervo


class JanelaBiblioteca(tk.Tk):
    def __init__(self, acervo: Acervo):
        super().__init__()
        self.acervo = acervo
        self.title("Biblioteca — Sistema de Acervo")
        self.geometry("720x460")
        self._montar()
        self._atualizar_tabela()
        # salva ao fechar a janela
        self.protocol("WM_DELETE_WINDOW", self._ao_fechar)

    # ------------------------------------------------------------
    def _montar(self):
        form = ttk.LabelFrame(self, text="Novo item", padding=10)
        form.pack(fill="x", padx=10, pady=8)

        self.var_tipo = tk.StringVar(value="Livro")
        ttk.Label(form, text="Tipo:").grid(row=0, column=0, sticky="w")
        combo = ttk.Combobox(form, textvariable=self.var_tipo,
                             values=["Livro", "DVD"], state="readonly",
                             width=10)
        combo.grid(row=0, column=1, sticky="w", padx=5)
        combo.bind("<<ComboboxSelected>>", lambda e: self._alternar_campos())

        campos = [("Código:", "codigo"), ("Título:", "titulo"),
                  ("Ano:", "ano"), ("Autor:", "autor"),
                  ("Páginas:", "paginas"), ("Duração (min):", "duracao")]
        self.entradas = {}
        for i, (rotulo, chave) in enumerate(campos):
            linha, col = divmod(i, 3)
            ttk.Label(form, text=rotulo).grid(row=linha + 1, column=col * 2,
                                              sticky="w", pady=2)
            e = ttk.Entry(form, width=18)
            e.grid(row=linha + 1, column=col * 2 + 1, padx=5, pady=2)
            self.entradas[chave] = e

        ttk.Button(form, text="Adicionar ao acervo",
                   command=self._adicionar).grid(row=0, column=5, padx=5)
        self._alternar_campos()

        acoes = ttk.Frame(self, padding=(10, 0))
        acoes.pack(fill="x")
        for texto, cmd in [("Emprestar", self._emprestar),
                           ("Devolver", self._devolver),
                           ("Remover", self._remover),
                           ("Salvar", self._salvar)]:
            ttk.Button(acoes, text=texto, command=cmd).pack(side="left", padx=3)

        cols = ("codigo", "tipo", "descricao", "prazo", "status")
        self.tabela = ttk.Treeview(self, columns=cols, show="headings",
                                   height=12)
        larguras = {"codigo": 70, "tipo": 60, "descricao": 340,
                    "prazo": 70, "status": 110}
        titulos = {"codigo": "Código", "tipo": "Tipo",
                   "descricao": "Descrição", "prazo": "Prazo",
                   "status": "Situação"}
        for c in cols:
            self.tabela.heading(c, text=titulos[c])
            self.tabela.column(c, width=larguras[c])
        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)

        self.status = ttk.Label(self, text="", anchor="w", padding=(10, 0))
        self.status.pack(fill="x", pady=(0, 6))

    def _alternar_campos(self):
        eh_livro = self.var_tipo.get() == "Livro"
        self.entradas["autor"].config(state="normal" if eh_livro else "disabled")
        self.entradas["paginas"].config(state="normal" if eh_livro else "disabled")
        self.entradas["duracao"].config(state="disabled" if eh_livro else "normal")

    # ------------------------------------------------------------
    def _adicionar(self):
        try:
            v = {k: e.get().strip() for k, e in self.entradas.items()}
            if self.var_tipo.get() == "Livro":
                item = Livro(v["codigo"], v["titulo"], int(v["ano"]),
                             v["autor"], int(v["paginas"]))
            else:
                item = DVD(v["codigo"], v["titulo"], int(v["ano"]),
                           int(v["duracao"]))
            self.acervo.adicionar(item)
            for e in self.entradas.values():
                e.delete(0, tk.END)
            self._atualizar_tabela(f"Item {item.codigo} adicionado.")
        except ValueError:
            messagebox.showerror("Dados inválidos",
                                 "Ano, páginas e duração devem ser números.")
        except ErroBiblioteca as erro:
            messagebox.showerror("Erro", str(erro))

    def _codigo_selecionado(self):
        sel = self.tabela.selection()
        if not sel:
            messagebox.showinfo("Selecione", "Escolha um item na tabela.")
            return None
        return self.tabela.item(sel[0], "values")[0]

    def _emprestar(self):
        codigo = self._codigo_selecionado()
        if not codigo:
            return
        try:
            item = self.acervo.buscar(codigo)
            item.emprestar()
            self._atualizar_tabela(
                f"'{item.titulo}' emprestado por {item.prazo_dias()} dias.")
        except ErroBiblioteca as erro:
            messagebox.showwarning("Não foi possível", str(erro))

    def _devolver(self):
        codigo = self._codigo_selecionado()
        if not codigo:
            return
        item = self.acervo.buscar(codigo)
        item.devolver()
        self._atualizar_tabela(f"'{item.titulo}' devolvido.")

    def _remover(self):
        codigo = self._codigo_selecionado()
        if not codigo:
            return
        if messagebox.askyesno("Confirmar", f"Remover o item {codigo}?"):
            self.acervo.remover(codigo)
            self._atualizar_tabela(f"Item {codigo} removido.")

    def _salvar(self):
        self.acervo.salvar()
        self._atualizar_tabela(f"Acervo salvo em {self.acervo.caminho}")

    def _atualizar_tabela(self, msg=""):
        self.tabela.delete(*self.tabela.get_children())
        for item in self.acervo:
            self.tabela.insert("", tk.END, values=(
                item.codigo,
                type(item).__name__,
                item.descricao(),
                f"{item.prazo_dias()} dias",
                "Emprestado" if item.emprestado else "Disponível",
            ))
        total = len(self.acervo)
        disp = len(self.acervo.disponiveis())
        self.status.config(text=f"{msg}   |   {total} itens ({disp} disponíveis)")

    def _ao_fechar(self):
        self.acervo.salvar()
        self.destroy()
