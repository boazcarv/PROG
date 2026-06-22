from datetime import datetime
import csv
import os

# 1 - REGISTRAR ENTRADA
def registrar_entrada(placa, veiculos_ativos):
    if placa in veiculos_ativos:
        print("❌ Veículo já está estacionado!")
        return False
    
    agora = datetime.now()
    veiculos_ativos[placa] = agora
    print(f"✓ Veículo {placa} entrou em {agora.strftime('%d/%m/%Y %H:%M:%S')}")
    return True


# 2 - REGISTRAR SAÍDA
def registrar_saida(placa, veiculos_ativos, historico):
    if placa not in veiculos_ativos:
        print("❌ Veículo não encontrado!")
        return False
    
    entrada = veiculos_ativos[placa]
    saida = datetime.now()
    tempo_horas = (saida - entrada).total_seconds() / 3600
    valor = max(10, tempo_horas * 15)  # R$ 15/hora, mínimo R$ 10
    
    historico.append({
        'placa': placa,
        'entrada': entrada,
        'saida': saida,
        'tempo': tempo_horas,
        'valor': valor
    })
    
    del veiculos_ativos[placa]
    print(f"✓ Veículo {placa}: {tempo_horas:.2f}h - Valor: R$ {valor:.2f}")
    return True


# 3 - LISTAR VEÍCULOS ATIVOS
def listar_veiculos(veiculos_ativos):
    if not veiculos_ativos:
        print("Estacionamento vazio")
        return
    
    print("\n" + "="*50)
    print("VEÍCULOS ESTACIONADOS")
    print("="*50)
    for placa, entrada in veiculos_ativos.items():
        tempo = (datetime.now() - entrada).total_seconds() / 3600
        print(f"  {placa}: {entrada.strftime('%d/%m/%Y %H:%M')} ({tempo:.2f}h)")
    print("="*50)


# 4 - SALVAR EM CSV
def salvar_csv(historico):
    with open('estacionamento_dados.csv', 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(['Placa', 'Entrada', 'Saída', 'Tempo (h)', 'Valor (R$)'])
        
        for reg in historico:
            escritor.writerow([
                reg['placa'],
                reg['entrada'].strftime('%d/%m/%Y %H:%M:%S'),
                reg['saida'].strftime('%d/%m/%Y %H:%M:%S'),
                f"{reg['tempo']:.2f}",
                f"{reg['valor']:.2f}"
            ])
    
    print("✓ Dados salvos em estacionamento_dados.csv")


# 5 - RELATÓRIO DE FATURAMENTO
def relatorio_faturamento(historico):
    if not historico:
        print("Sem registros para relatório")
        return
    
    faturamento = {}
    
    for reg in historico:
        mes = reg['saida'].strftime('%m/%Y')
        if mes not in faturamento:
            faturamento[mes] = 0
        faturamento[mes] += reg['valor']
    
    print("\n" + "="*50)
    print("FATURAMENTO POR MÊS")
    print("="*50)
    total = 0
    for mes in sorted(faturamento.keys()):
        valor = faturamento[mes]
        total += valor
        print(f"  {mes}: R$ {valor:.2f}")
    print(f"  TOTAL: R$ {total:.2f}")
    print("="*50)
    
    # Salvar em arquivo txt
    with open('relatorio_faturamento.txt', 'w', encoding='utf-8') as f:
        f.write("RELATÓRIO DE FATURAMENTO\n")
        f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("="*50 + "\n\n")
        for mes in sorted(faturamento.keys()):
            f.write(f"{mes}: R$ {faturamento[mes]:.2f}\n")
        f.write(f"\nTOTAL: R$ {total:.2f}\n")
    
    print("✓ Relatório salvo em relatorio_faturamento.txt")


# 6 - MENU PRINCIPAL
def main():
    veiculos_ativos = {}
    historico = []
    
    while True:
        print("\n" + "="*50)
        print("GERENCIAMENTO DE ESTACIONAMENTO")
        print("="*50)
        print("1. Entrada de veículo")
        print("2. Saída de veículo")
        print("3. Ver veículos estacionados")
        print("4. Relatório de faturamento")
        print("5. Salvar dados")
        print("6. Sair")
        print("="*50)
        
        opcao = input("Opção: ").strip()
        
        if opcao == "1":
            placa = input("Placa: ").strip().upper()
            registrar_entrada(placa, veiculos_ativos)
        
        elif opcao == "2":
            placa = input("Placa: ").strip().upper()
            registrar_saida(placa, veiculos_ativos, historico)
        
        elif opcao == "3":
            listar_veiculos(veiculos_ativos)
        
        elif opcao == "4":
            relatorio_faturamento(historico)
        
        elif opcao == "5":
            salvar_csv(historico)
        
        elif opcao == "6":
            print("Até logo!")
            break
        
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
