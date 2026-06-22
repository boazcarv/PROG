import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
import csv
import os

class EstacionamentoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🅿️ Gerenciamento de Estacionamento")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Dados
        self.veiculos_ativos = {}
        self.historico = []
        
        # Cores
        self.cor_bg = "#f0f0f0"
        self.cor_primaria = "#2c3e50"
        self.cor_sucesso = "#27ae60"
        self.cor_erro = "#e74c3c"
        
        self.root.configure(bg=self.cor_bg)
        
        self.criar_interface()
    
    def criar_interface(self):
        # Header
        header = tk.Frame(self.root, bg=self.cor_primaria, height=80)
        header.pack(fill=tk.X)
        
        titulo = tk.Label(header, text="🅿️ ESTACIONAMENTO", 
                         font=("Arial", 24, "bold"), 
                         fg="white", bg=self.cor_primaria)
        titulo.pack(pady=10)
        
        # Notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Aba 1: Entrada/Saída
        self.aba_movimentacao()
        
        # Aba 2: Veículos Ativos
        self.aba_veiculos_ativos()
        
        # Aba 3: Relatório
        self.aba_relatorio()
        
        # Aba 4: Dados
        self.aba_dados()
    
    def aba_movimentacao(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📍 Entrada/Saída")
        
        # Frame Entrada
        frame_entrada = tk.LabelFrame(frame, text="ENTRADA DE VEÍCULO", 
                                     font=("Arial", 12, "bold"), padx=20, pady=20)
        frame_entrada.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(frame_entrada, text="Placa do veículo:", 
                font=("Arial", 11)).pack(anchor=tk.W)
        
        self.entrada_placa_entrada = tk.Entry(frame_entrada, font=("Arial", 12), width=20)
        self.entrada_placa_entrada.pack(pady=5)
        self.entrada_placa_entrada.bind("<Return>", lambda e: self.btn_entrada_click())
        
        tk.Button(frame_entrada, text="✓ Registrar Entrada", 
                 command=self.btn_entrada_click,
                 font=("Arial", 11, "bold"), 
                 bg=self.cor_sucesso, fg="white", padx=20, pady=10).pack(pady=10)
        
        # Frame Saída
        frame_saida = tk.LabelFrame(frame, text="SAÍDA DE VEÍCULO", 
                                   font=("Arial", 12, "bold"), padx=20, pady=20)
        frame_saida.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(frame_saida, text="Placa do veículo:", 
                font=("Arial", 11)).pack(anchor=tk.W)
        
        self.entrada_placa_saida = tk.Entry(frame_saida, font=("Arial", 12), width=20)
        self.entrada_placa_saida.pack(pady=5)
        self.entrada_placa_saida.bind("<Return>", lambda e: self.btn_saida_click())
        
        tk.Button(frame_saida, text="✗ Registrar Saída", 
                 command=self.btn_saida_click,
                 font=("Arial", 11, "bold"), 
                 bg=self.cor_erro, fg="white", padx=20, pady=10).pack(pady=10)
        
        # Informações
        frame_info = tk.LabelFrame(frame, text="INFORMAÇÕES", 
                                  font=("Arial", 11, "bold"), padx=20, pady=15)
        frame_info.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.label_info = tk.Label(frame_info, text="Aguardando operações...", 
                                  font=("Arial", 10), justify=tk.LEFT)
        self.label_info.pack(anchor=tk.W)
    
    def aba_veiculos_ativos(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="🚗 Veículos Ativos")
        
        # Botão atualizar
        tk.Button(frame, text="🔄 Atualizar", command=self.atualizar_veiculos,
                 font=("Arial", 10, "bold"), bg="#3498db", fg="white").pack(pady=10)
        
        # Área de texto
        self.texto_veiculos = scrolledtext.ScrolledText(frame, font=("Courier", 10), 
                                                        height=20, width=80)
        self.texto_veiculos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.texto_veiculos.config(state=tk.DISABLED)
        
        self.atualizar_veiculos()
    
    def aba_relatorio(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📊 Relatório")
        
        # Botão gerar
        tk.Button(frame, text="📋 Gerar Relatório", command=self.gerar_relatorio,
                 font=("Arial", 10, "bold"), bg="#9b59b6", fg="white").pack(pady=10)
        
        # Área de texto
        self.texto_relatorio = scrolledtext.ScrolledText(frame, font=("Courier", 10), 
                                                        height=20, width=80)
        self.texto_relatorio.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.texto_relatorio.config(state=tk.DISABLED)
    
    def aba_dados(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="💾 Dados")
        
        # Botões
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text="💾 Salvar em CSV", command=self.salvar_csv,
                 font=("Arial", 10, "bold"), bg=self.cor_sucesso, fg="white", 
                 padx=15, pady=10).pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="📄 Salvar Relatório", command=self.salvar_relatorio,
                 font=("Arial", 10, "bold"), bg="#f39c12", fg="white", 
                 padx=15, pady=10).pack(side=tk.LEFT, padx=5)
        
        # Área de texto
        self.texto_dados = scrolledtext.ScrolledText(frame, font=("Courier", 9), 
                                                    height=20, width=80)
        self.texto_dados.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.texto_dados.config(state=tk.DISABLED)
        
        self.atualizar_dados()
    
    # Funções de Lógica
    def registrar_entrada(self, placa):
        if placa in self.veiculos_ativos:
            return False, "❌ Veículo já está estacionado!"
        
        agora = datetime.now()
        self.veiculos_ativos[placa] = agora
        msg = f"✓ Veículo {placa} entrou em {agora.strftime('%d/%m/%Y %H:%M:%S')}"
        return True, msg
    
    def registrar_saida(self, placa):
        if placa not in self.veiculos_ativos:
            return False, "❌ Veículo não encontrado!"
        
        entrada = self.veiculos_ativos[placa]
        saida = datetime.now()
        tempo_horas = (saida - entrada).total_seconds() / 3600
        valor = max(10, tempo_horas * 15)
        
        self.historico.append({
            'placa': placa,
            'entrada': entrada,
            'saida': saida,
            'tempo': tempo_horas,
            'valor': valor
        })
        
        del self.veiculos_ativos[placa]
        msg = f"✓ Veículo {placa}: {tempo_horas:.2f}h - Valor: R$ {valor:.2f}"
        return True, msg
    
    def listar_veiculos(self):
        if not self.veiculos_ativos:
            return "Estacionamento vazio"
        
        texto = "="*50 + "\n"
        texto += "VEÍCULOS ESTACIONADOS\n"
        texto += "="*50 + "\n"
        for placa, entrada in self.veiculos_ativos.items():
            tempo = (datetime.now() - entrada).total_seconds() / 3600
            texto += f"  {placa}: {entrada.strftime('%d/%m/%Y %H:%M')} ({tempo:.2f}h)\n"
        texto += "="*50
        return texto
    
    def relatorio_faturamento(self):
        if not self.historico:
            return "Sem registros para relatório"
        
        faturamento = {}
        
        for reg in self.historico:
            mes = reg['saida'].strftime('%m/%Y')
            if mes not in faturamento:
                faturamento[mes] = 0
            faturamento[mes] += reg['valor']
        
        texto = "="*50 + "\n"
        texto += "FATURAMENTO POR MÊS\n"
        texto += "="*50 + "\n"
        total = 0
        for mes in sorted(faturamento.keys()):
            valor = faturamento[mes]
            total += valor
            texto += f"  {mes}: R$ {valor:.2f}\n"
        texto += f"  TOTAL: R$ {total:.2f}\n"
        texto += "="*50
        return texto
    
    # Callbacks dos Botões
    def btn_entrada_click(self):
        placa = self.entrada_placa_entrada.get().strip().upper()
        
        if not placa:
            messagebox.showwarning("Aviso", "Digite uma placa!")
            return
        
        sucesso, msg = self.registrar_entrada(placa)
        
        if sucesso:
            messagebox.showinfo("Sucesso", msg)
            self.entrada_placa_entrada.delete(0, tk.END)
            self.label_info.config(text=msg, fg=self.cor_sucesso)
            self.atualizar_veiculos()
            self.atualizar_dados()
        else:
            messagebox.showerror("Erro", msg)
            self.label_info.config(text=msg, fg=self.cor_erro)
    
    def btn_saida_click(self):
        placa = self.entrada_placa_saida.get().strip().upper()
        
        if not placa:
            messagebox.showwarning("Aviso", "Digite uma placa!")
            return
        
        sucesso, msg = self.registrar_saida(placa)
        
        if sucesso:
            messagebox.showinfo("Sucesso", msg)
            self.entrada_placa_saida.delete(0, tk.END)
            self.label_info.config(text=msg, fg=self.cor_sucesso)
            self.atualizar_veiculos()
            self.atualizar_dados()
        else:
            messagebox.showerror("Erro", msg)
            self.label_info.config(text=msg, fg=self.cor_erro)
    
    def atualizar_veiculos(self):
        self.texto_veiculos.config(state=tk.NORMAL)
        self.texto_veiculos.delete(1.0, tk.END)
        self.texto_veiculos.insert(1.0, self.listar_veiculos())
        self.texto_veiculos.config(state=tk.DISABLED)
    
    def gerar_relatorio(self):
        self.texto_relatorio.config(state=tk.NORMAL)
        self.texto_relatorio.delete(1.0, tk.END)
        self.texto_relatorio.insert(1.0, self.relatorio_faturamento())
        self.texto_relatorio.config(state=tk.DISABLED)
    
    def atualizar_dados(self):
        self.texto_dados.config(state=tk.NORMAL)
        self.texto_dados.delete(1.0, tk.END)
        
        texto = "HISTÓRICO DE TRANSAÇÕES\n"
        texto += "="*60 + "\n"
        
        if not self.historico:
            texto += "Nenhum registro ainda.\n"
        else:
            for reg in self.historico:
                texto += f"\nPlaca: {reg['placa']}\n"
                texto += f"Entrada: {reg['entrada'].strftime('%d/%m/%Y %H:%M:%S')}\n"
                texto += f"Saída: {reg['saida'].strftime('%d/%m/%Y %H:%M:%S')}\n"
                texto += f"Tempo: {reg['tempo']:.2f}h\n"
                texto += f"Valor: R$ {reg['valor']:.2f}\n"
                texto += "-"*60 + "\n"
        
        self.texto_dados.insert(1.0, texto)
        self.texto_dados.config(state=tk.DISABLED)
    
    def salvar_csv(self):
        if not self.historico:
            messagebox.showwarning("Aviso", "Nenhum dado para salvar!")
            return
        
        with open('estacionamento_dados.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(['Placa', 'Entrada', 'Saída', 'Tempo (h)', 'Valor (R$)'])
            
            for reg in self.historico:
                escritor.writerow([
                    reg['placa'],
                    reg['entrada'].strftime('%d/%m/%Y %H:%M:%S'),
                    reg['saida'].strftime('%d/%m/%Y %H:%M:%S'),
                    f"{reg['tempo']:.2f}",
                    f"{reg['valor']:.2f}"
                ])
        
        messagebox.showinfo("Sucesso", "✓ Dados salvos em estacionamento_dados.csv")
    
    def salvar_relatorio(self):
        if not self.historico:
            messagebox.showwarning("Aviso", "Nenhum dado para gerar relatório!")
            return
        
        faturamento = {}
        
        for reg in self.historico:
            mes = reg['saida'].strftime('%m/%Y')
            if mes not in faturamento:
                faturamento[mes] = 0
            faturamento[mes] += reg['valor']
        
        with open('relatorio_faturamento.txt', 'w', encoding='utf-8') as f:
            f.write("RELATÓRIO DE FATURAMENTO\n")
            f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write("="*50 + "\n\n")
            total = 0
            for mes in sorted(faturamento.keys()):
                valor = faturamento[mes]
                total += valor
                f.write(f"{mes}: R$ {valor:.2f}\n")
            f.write(f"\nTOTAL: R$ {total:.2f}\n")
        
        messagebox.showinfo("Sucesso", "✓ Relatório salvo em relatorio_faturamento.txt")


if __name__ == "__main__":
    root = tk.Tk()
    app = EstacionamentoGUI(root)
    root.mainloop()
