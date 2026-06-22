"""
============================================================
ARQUIVO: interface.py
Interface Gráfica - conecta no estacionamento.py
============================================================
Este arquivo IMPORTA as funções do estacionamento.py
============================================================
"""

from tkinter import *
from tkinter import ttk, messagebox
import estacionamento


# ============================================================
# AÇÕES DOS BOTÕES
# ============================================================

def atualizar_tabela():
    """Atualiza a tabela de vagas"""
    vagas = estacionamento.ler_vagas()
    
    # Limpa a tabela
    for row in tabela.get_children():
        tabela.delete(row)
    
    # Adiciona as vagas
    for v in vagas:
        estado = "🟢 Livre" if v["estado"] == "livre" else "🔴 Ocupado"
        entrada = v["entrada"] if v["entrada"] != "none" else "---"
        saida = v["saida"] if v["saida"] != "none" else "---"
        
        tabela.insert("", END, values=(v["vaga"], estado, v["placa"], entrada, saida))


def acao_criar_vagas():
    """Cria vagas"""
    try:
        qtd = int(entry_qtd.get())
        if qtd > 0:
            estacionamento.criar_vagas_iniciais(qtd)
            messagebox.showinfo("Sucesso", f"{qtd} vagas criadas!")
            entry_qtd.delete(0, END)
            atualizar_tabela()
        else:
            messagebox.showerror("Erro", "Digite um número válido!")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números!")


def acao_entrada():
    """Registra entrada"""
    placa = entry_placa.get().strip().upper()
    
    if not placa:
        messagebox.showerror("Erro", "Digite a placa!")
        return
    
    sucesso, mensagem = estacionamento.registrar_entrada(placa)
    
    if sucesso:
        messagebox.showinfo("Sucesso", mensagem)
        entry_placa.delete(0, END)
        atualizar_tabela()
    else:
        messagebox.showerror("Erro", mensagem)


def acao_saida():
    """Registra saída"""
    sucesso, mensagem = estacionamento.registrar_saida()
    
    if sucesso:
        messagebox.showinfo("Sucesso", mensagem)
        atualizar_tabela()
    else:
        messagebox.showerror("Erro", mensagem)


def acao_relatorio():
    """Gera relatório"""
    sucesso, mensagem = estacionamento.gerar_relatorio()
    
    if sucesso:
        nome_arquivo = estacionamento.salvar_relatorio_arquivo()
        messagebox.showinfo("Relatório", f"{mensagem}\n\nSalvo em: {nome_arquivo}")
    else:
        messagebox.showerror("Erro", mensagem)


# ============================================================
# CRIAR JANELA
# ============================================================

janela = Tk()
janela.title(" parking - Sistema de Estacionamento")
janela.geometry("800x600")
janela.configure(bg="#2c3e50")

# ============================================================
# TÍTULO
# ============================================================

Label(janela, text="SISTEMA DE ESTACIONAMENTO", 
      font=("Arial", 20, "bold"), fg="white", bg="#2c3e50").pack(pady=20)

# ============================================================
# BOTÕES
# ============================================================

frame_botoes = Frame(janela, bg="#2c3e50")
frame_botoes.pack(pady=10)

# Criar Vagas
frame_criar = Frame(frame_botoes, bg="#34495e", padx=15, pady=10)
frame_criar.grid(row=0, column=0, padx=10)

Label(frame_criar, text="Criar Vagas", bg="#34495e", fg="#27ae60", 
      font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

Label(frame_criar, text="Quantidade:", bg="#34495e", fg="white", 
      font=("Arial", 10)).grid(row=1, column=0, pady=5, sticky=W)

entry_qtd = Entry(frame_criar, width=10, font=("Arial", 14))
entry_qtd.grid(row=1, column=1, pady=5, padx=5)

Button(frame_criar, text="Criar", bg="#27ae60", fg="white", 
       font=("Arial", 10, "bold"), command=acao_criar_vagas).grid(row=2, column=0, columnspan=2, pady=10)

# Entrada
frame_entrada = Frame(frame_botoes, bg="#34495e", padx=15, pady=10)
frame_entrada.grid(row=0, column=1, padx=10)

Label(frame_entrada, text="Entrada", bg="#34495e", fg="#f39c12", 
      font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

Label(frame_entrada, text="Placa:", bg="#34495e", fg="white", 
      font=("Arial", 10)).grid(row=1, column=0, pady=5, sticky=W)

entry_placa = Entry(frame_entrada, width=15, font=("Arial", 14))
entry_placa.grid(row=1, column=1, pady=5, padx=5)

Button(frame_entrada, text="Registrar Entrada 🚗", bg="#f39c12", fg="white", 
       font=("Arial", 10, "bold"), command=acao_entrada).grid(row=2, column=0, columnspan=2, pady=10)

# Saída
frame_saida = Frame(frame_botoes, bg="#34495e", padx=15, pady=10)
frame_saida.grid(row=0, column=2, padx=10)

Label(frame_saida, text="Saída", bg="#34495e", fg="#e74c3c", 
      font=("Arial", 11, "bold")).pack(pady=5)

Button(frame_saida, text="Registrar Saída 🚙", bg="#e74c3c", fg="white", 
       font=("Arial", 11, "bold"), command=acao_saida).pack(pady=15, padx=20)

# Relatório
frame_relatorio = Frame(frame_botoes, bg="#34495e", padx=15, pady=10)
frame_relatorio.grid(row=0, column=3, padx=10)

Label(frame_relatorio, text="Relatório", bg="#34495e", fg="#3498db", 
      font=("Arial", 11, "bold")).pack(pady=5)

Button(frame_relatorio, text="Ver Relatório 📊", bg="#3498db", fg="white", 
       font=("Arial", 11, "bold"), command=acao_relatorio).pack(pady=15, padx=20)

# ============================================================
# TABELA
# ============================================================

Label(janela, text="VAGAS DO ESTACIONAMENTO", bg="#2c3e50", fg="white", 
      font=("Arial", 14, "bold")).pack(pady=10)

frame_tabela = Frame(janela)
frame_tabela.pack(pady=10)

scrollbar_y = Scrollbar(frame_tabela, orient=VERTICAL)
scrollbar_y.pack(side=RIGHT, fill=Y)

tabela = ttk.Treeview(frame_tabela, columns=("vaga", "estado", "placa", "entrada", "saida"),
                       show="headings", height=15, yscrollcommand=scrollbar_y.set)

scrollbar_y.config(command=tabela.yview)

tabela.heading("vaga", text="Vaga")
tabela.heading("estado", text="Estado")
tabela.heading("placa", text="Placa")
tabela.heading("entrada", text="Entrada")
tabela.heading("saida", text="Saída")

tabela.column("vaga", width=60, anchor=CENTER)
tabela.column("estado", width=100, anchor=CENTER)
tabela.column("placa", width=120, anchor=CENTER)
tabela.column("entrada", width=150, anchor=CENTER)
tabela.column("saida", width=150, anchor=CENTER)

tabela.pack(side=LEFT, fill=BOTH, expand=True)

# ============================================================
# BOTÃO ATUALIZAR
# ============================================================

Button(janela, text="🔄 Atualizar Tabela", bg="#95a5a6", fg="white",
       font=("Arial", 10), command=atualizar_tabela).pack(pady=10)

# ============================================================
# INICIAR
# ============================================================

atualizar_tabela()
janela.mainloop()