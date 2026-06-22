"""
============================================================
ARQUIVO: estacionamento.py
Lógica completa do Sistema de Estacionamento
============================================================
Este arquivo contém TODAS as funções do sistema.
A interface gráfica vai importar daqui.
============================================================
"""

import csv
from datetime import datetime


# ============================================================
# FUNÇÕES DE DADOS (CSV)
# ============================================================

def ler_vagas():
    """Lê todas as vagas do arquivo CSV"""
    vagas = []
    try:
        with open("vagas.csv", "r", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo, delimiter=";")
            for row in reader:
                vagas.append(row)
    except FileNotFoundError:
        return []
    return vagas


def salvar_vagas(vagas):
    """Salva a lista de vagas de volta no arquivo CSV"""
    with open("vagas.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerow(["vaga", "estado", "placa", "entrada", "saida"])
        for v in vagas:
            writer.writerow([v["vaga"], v["estado"], v["placa"], v["entrada"], v["saida"]])


def criar_vagas_iniciais(qtd):
    """Cria a estrutura inicial das vagas no CSV"""
    lista = [["vaga", "estado", "placa", "entrada", "saida"]]
    
    for i in range(qtd):
        lista.append([str(i + 1), "livre", "none", "none", "none"])
    
    with open("vagas.csv", "w", newline="", encoding="utf-8") as arquivo:
        csv_dados = csv.writer(arquivo, delimiter=";")
        for elemento in lista:
            csv_dados.writerow(elemento)
    
    return True


# ============================================================
# FUNÇÕES DE ENTRADA E SAÍDA
# ============================================================

def registrar_entrada(placa):
    """Registra a entrada de um veículo"""
    vagas = ler_vagas()
    
    if not vagas:
        return False, "Nenhuma vaga criada!"
    
    # Busca vaga livre
    vaga = None
    for v in vagas:
        if v["estado"] == "livre":
            vaga = v
            break
    
    if not vaga:
        return False, "Não há vagas disponíveis!"
    
    # Verifica se placa já está em uso
    for v in vagas:
        if v["placa"] == placa and v["estado"] == "ocupado":
            return False, f"Veículo {placa} já está estacionado!"
    
    # Registra entrada
    hora_entrada = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    vaga["estado"] = "ocupado"
    vaga["placa"] = placa
    vaga["entrada"] = hora_entrada
    
    salvar_vagas(vagas)
    
    return True, f"Entrada registrada!\nVaga: {vaga['vaga']}\nPlaca: {placa}"


def registrar_saida():
    """Registra a saída de um veículo"""
    vagas = ler_vagas()
    
    if not vagas:
        return False, "Nenhuma vaga criada!"
    
    # Busca vaga ocupada
    vaga = None
    for v in vagas:
        if v["estado"] == "ocupado":
            vaga = v
            break
    
    if not vaga:
        return False, "Não há veículos estacionados!"
    
    # Calcula tempo e valor
    hora_saida = datetime.now().strftime("%d/%m/%Y %H:%M")
    formato = "%d/%m/%Y %H:%M"
    
    entrada_dt = datetime.strptime(vaga["entrada"], formato)
    saida_dt = datetime.strptime(hora_saida, formato)
    
    horas = (saida_dt - entrada_dt).total_seconds() / 3600
    if horas < 1:
        horas = 1
    
    valor = horas * 5.00
    
    # Atualiza vaga
    vaga["estado"] = "livre"
    vaga["saida"] = hora_saida
    
    salvar_vagas(vagas)
    
    return True, f"Saída registrada!\nVaga: {vaga['vaga']}\nPlaca: {vaga['placa']}\nTempo: {int(horas)}h\nValor: R$ {valor:.2f}"


# ============================================================
# FUNÇÕES DE RELATÓRIOS
# ============================================================

def gerar_relatorio():
    """Gera relatório de faturamento"""
    vagas = ler_vagas()
    
    if not vagas:
        return False, "Nenhuma vaga criada!"
    
    total_veiculos = 0
    total_valor = 0.0
    
    for v in vagas:
        if v["estado"] == "livre" and v["saida"] != "none":
            if v["entrada"] != "none" and v["saida"] != "none":
                formato = "%d/%m/%Y %H:%M"
                entrada_dt = datetime.strptime(v["entrada"], formato)
                saida_dt = datetime.strptime(v["saida"], formato)
                
                horas = (saida_dt - entrada_dt).total_seconds() / 3600
                if horas < 1:
                    horas = 1
                
                total_veiculos += 1
                total_valor += horas * 5.00
    
    return True, f"Faturamento Total\n\nVeículos atendidos: {total_veiculos}\nTotal: R$ {total_valor:.2f}"


def salvar_relatorio_arquivo():
    """Salva relatório em arquivo de texto"""
    vagas = ler_vagas()
    
    total_veiculos = 0
    total_valor = 0.0
    
    for v in vagas:
        if v["estado"] == "livre" and v["saida"] != "none":
            if v["entrada"] != "none" and v["saida"] != "none":
                formato = "%d/%m/%Y %H:%M"
                entrada_dt = datetime.strptime(v["entrada"], formato)
                saida_dt = datetime.strptime(v["saida"], formato)
                
                horas = (saida_dt - entrada_dt).total_seconds() / 3600
                if horas < 1:
                    horas = 1
                
                total_veiculos += 1
                total_valor += horas * 5.00
    
    nome_arquivo = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("   RELATÓRIO DE FATURAMENTO\n")
        f.write("=" * 40 + "\n")
        f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        f.write(f"Veículos: {total_veiculos}\n")
        f.write(f"Total: R$ {total_valor:.2f}\n")
        f.write("=" * 40 + "\n")
    
    return nome_arquivo


# ============================================================
# MENU (modo texto)
# ============================================================

def menu():
    """Mostra o menu principal"""
    print("\n" + "=" * 50)
    print("   SISTEMA DE ESTACIONAMENTO")
    print("=" * 50)
    print("  1 - Criar vagas")
    print("  2 - Ver vagas")
    print("  3 - Registrar entrada")
    print("  4 - Registrar saída")
    print("  5 - Relatório")
    print("  0 - Sair")
    print("-" * 50)


def main():
    """Função principal - modo texto"""
    print("\n🐍 SISTEMA DE ESTACIONAMENTO\n")
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            qtd = int(input("Quantidade de vagas: "))
            criar_vagas_iniciais(qtd)
            print("✓ Vagas criadas!")
            
        elif opcao == "2":
            vagas = ler_vagas()
            print("\nVAGAS:")
            for v in vagas:
                estado = "livre" if v["estado"] == "livre" else "ocupado"
                print(f"  Vaga {v['vaga']}: {estado} - {v['placa']}")
                
        elif opcao == "3":
            placa = input("Placa: ").strip().upper()
            sucesso, msg = registrar_entrada(placa)
            print(msg)
            
        elif opcao == "4":
            sucesso, msg = registrar_saida()
            print(msg)
            
        elif opcao == "5":
            sucesso, msg = gerar_relatorio()
            print(msg)
            nome = salvar_relatorio_arquivo()
            print(f"Salvo em: {nome}")
            
        elif opcao == "0":
            print("\nSaindo... 👋")
            break
        
        input("\nPressione ENTER...")


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":
    main()