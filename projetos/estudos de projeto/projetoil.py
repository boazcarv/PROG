# ============================================================
# SISTEMA DE GERENCIAMENTO DE ESTACIONAMENTO
# Projeto da disciplina de Introdução à Lógica e Programação
# ============================================================

# Este programa gerencia um estacionamento com as seguintes funcionalidades:
# - Criar vagas iniciais (salva em arquivo CSV)
# - Registrar entrada de veículos (placa + horário)
# - Registrar saída de veículos (calcula tempo e valor a pagar)
# - Relatório de veículos estacionados no momento
# - Relatório de faturamento (mensal, semanal e total)
# - Interface gráfica com Tkinter

# Arquivos CSV utilizados:
# - vagas.csv          → armazena o estado atual de cada vaga
# - historico_saida.csv → registra cada saída (placa, entrada, saída, valor)
# - relatorio_do_faturamento.csv → relatório gerado de faturamento
# ============================================================


# ============================================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ============================================================

import csv  # Biblioteca para ler e escrever arquivos CSV (Comma Separated Values)
# CSV é um formato de arquivo de texto onde os dados são separados por ponto e vírgula (;)
# ou vírgula (,). Cada linha é um registro e cada coluna é um campo.
# Exemplo de arquivo CSV:
#   vaga;estado;placa;entrada;saida
#   1;livre;none;none;none
#   2;ocupado;ABC-1234;06/07/2026 14:30;none

from datetime import datetime  # Biblioteca para trabalhar com datas e horários
# datetime.now()        → pega a data/hora atual do computador
# datetime.strptime()   → converte uma STRING em um objeto de data/hora
# datetime.strftime()   → converte um objeto de data/hora em STRING formatada

import os  # Biblioteca para interagir com o sistema operacional
# os.path.exists() → verifica se um arquivo ou pasta existe no computador


# ============================================================
# PARTE 1: ESTRUTURA INICIAL (criado pelo membro original)
# ============================================================
# Esta função cria o arquivo CSV com as vagas do estacionamento.
# Cada vaga começa como "livre", sem placa nem horário.
# ============================================================


def criar_vagas_iniciais():
    """Cria o arquivo vagas.csv com a quantidade de vagas informada pelo usuário."""

    # Pergunta ao usuário quantas vagas o estacionamento terá
    # int() converte a string digitada para número inteiro
    qvagas = int(input("digite a quantidade de vagas: "))  # Ex: se digitar 5, qvagas = 5

    # Cria o cabeçalho da tabela — a primeira linha do CSV
    # Cada sublista representa uma coluna: vaga, estado, placa, entrada, saida
    lista = [
        ["vaga", "estado", "placa", "entrada", "saida"]
    ]
    # Neste ponto, lista = [["vaga", "estado", "placa", "entrada", "saida"]]

    # Cria as linhas da tabela, uma para cada vaga
    # range(qvagas) gera os números de 0 até qvagas-1
    # i + 1 ajusta para que a numeração comece em 1 (não em 0)
    for i in range(qvagas):  # Se qvagas=3: i será 0, 1, 2
        indice = str(i + 1)  # Converte para string: "1", "2", "3"
        # += adiciona uma nova sublista ao final da lista principal
        # Cada vaga começa: número, "livre", sem placa ("none"), sem horários ("none")
        lista += [[indice, "livre", "none", "none", "none"]]

    # Após o loop, se qvagas=3, lista será:
    # [["vaga", "estado", "placa", "entrada", "saida"],
    #  ["1", "livre", "none", "none", "none"],
    #  ["2", "livre", "none", "none", "none"],
    #  ["3", "livre", "none", "none", "none"]]

    # Imprime cada linha da tabela na tela (apenas para visualização)
    for elemento in lista:
        print(elemento)  # Ex: ['1', 'livre', 'none', 'none', 'none']

    # Abre (ou cria) o arquivo "vagas.csv" no modo de escrita ("w" = write)
    # newline="" evita que o Python adicione linhas em branco extras entre os registros
    # (problema comum no Windows ao escrever CSV)
    arquivo = open("vagas.csv", "w", newline="")

    # -------------------------------------------------------
    # Comentário: forma alternativa SEM a biblioteca csv
    # -------------------------------------------------------
    # Sem a biblioteca csv, teríamos que montar cada linha manualmente:
    # for elemento in lista:
    #     csv_dados = ";".join(elemento)  # Junta os itens com ";" entre eles
    #     arquivo.write(csv_dados + "\n")  # Escreve a linha e pula para a próxima
    #
    # Exemplo: ["1", "livre", "none", "none", "none"]
    #          → "1;livre;none;none;none\n"
    # -------------------------------------------------------

    # Usando a biblioteca csv para escrever os dados (forma mais profissional)
    # csv.writer() cria um objeto que sabe escrever dados no formato CSV
    # delimiter=";" define que o separador de colunas será ponto e vírgula
    # (No Brasil, usamos ";" em vez de "," porque nossos decimais usam vírgula)
    csv_dados = csv.writer(arquivo, delimiter=";")

    # Percorre cada linha da lista e escreve no arquivo CSV
    # writerow() transforma uma lista em uma linha do CSV
    # ["1", "livre", "none", "none", "none"] → "1;livre;none;none;none"
    for elemento in lista:
        csv_dados.writerow(elemento)

    # Fecha o arquivo — MUITO IMPORTANTE!
    # Se não fechar, os dados podem não ser salvos (ficam no buffer de memória)
    arquivo.close()


# ============================================================
# PARTE 2: FUNÇÕES DE LEITURA DO CSV
# ============================================================
# Estas funções leem e salvam os dados no arquivo vagas.csv.
# Todas as outras funções dependem delas para acessar os dados.
# ============================================================


def ler_vagas():
    """Lê todas as vagas do arquivo CSV e retorna como uma lista de dicionários."""

    vagas = []  # Lista vazia que vai armazenar todas as vagas lidas do arquivo

    # try/except é uma estrutura de tratamento de erros:
    # - try: tenta executar o código
    # - except: se der erro, executa o código alternativo
    try:
        # Abre o arquivo "vagas.csv" no modo leitura ("r" = read)
        # with é um "gerenciador de contexto" — fecha o arquivo automaticamente ao sair do bloco
        # encoding="utf-8" garante que caracteres especiais (acentos, emojis) sejam lidos corretamente
        with open("vagas.csv", "r", encoding="utf-8") as arquivo:

            # csv.DictReader() lê o CSV e transforma cada linha em um DICIONÁRIO
            # Usa a primeira linha como cabeçalho (chaves do dicionário)
            # delimiter=";" indica que o separador é ponto e vírgula
            # Exemplo de resultado:
            #   {"vaga": "1", "estado": "livre", "placa": "none", "entrada": "none", "saida": "none"}
            reader = csv.DictReader(arquivo, delimiter=";")

            # Percorre cada linha (dicionário) do arquivo e adiciona à lista
            for row in reader:
                vagas.append(row)
                # Após o loop, vagas será algo como:
                # [{"vaga":"1", "estado":"livre", ...},
                #  {"vaga":"2", "estado":"ocupado", ...}, ...]

    except FileNotFoundError:
        # Se o arquivo não existe (ninguém criou as vagas ainda), mostra mensagem de erro
        print("Erro: Arquivo vagas.csv não encontrado!")
        print("Execute a opção 1 primeiro para criar as vagas.")

    # Retorna a lista de dicionários (cada dicionário = uma vaga)
    return vagas


def salvar_vagas(vagas):
    """Salva a lista de vagas de volta no arquivo CSV, sobrescrevendo o arquivo anterior."""

    # Abre o arquivo no modo escrita ("w") — isso APAGA o conteúdo anterior!
    # newline="" evita linhas em branco extras
    # encoding="utf-8" para suportar caracteres especiais
    with open("vagas.csv", "w", newline="", encoding="utf-8") as arquivo:

        # Cria o objeto writer para escrever no CSV
        writer = csv.writer(arquivo, delimiter=";")

        # Escreve o cabeçalho (primeira linha do CSV)
        # É obrigatório reescrever o cabeçalho pois o modo "w" apagou tudo
        writer.writerow(["vaga", "estado", "placa", "entrada", "saida"])

        # Percorre cada vaga (dicionário) e escreve como linha no CSV
        # v["vaga"], v["estado"], etc. acessam os valores do dicionário pela chave
        for v in vagas:
            writer.writerow([v["vaga"], v["estado"], v["placa"], v["entrada"], v["saida"]])
            # Exemplo: writer.writerow(["1", "ocupado", "ABC-1234", "06/07/2026 14:30", "none"])
            # Resultado no CSV: 1;ocupado;ABC-1234;06/07/2026 14:30;none


# ============================================================
# PARTE 3: REGISTRO DE ENTRADA
# ============================================================
# Registra a entrada de um veículo: escolhe vaga livre, digita placa,
# registra horário e atualiza o arquivo CSV.
# ============================================================


def registrar_entrada():
    """Registra a entrada de um veículo no estacionamento."""

    # Lê todas as vagas do arquivo CSV (lista de dicionários)
    vagas = ler_vagas()

    print("\n--- REGISTRAR ENTRADA ---")

    # Mostra apenas as vagas que estão livres (disponíveis para uso)
    print("\nVagas disponíveis:")
    vagas_livres = []  # Lista para armazenar apenas as vagas com estado "livre"

    # Percorre TODAS as vagas
    for v in vagas:
        if v["estado"] == "livre":  # Filtra só as vagas livres
            print(f"  Vaga {v['vaga']}")  # Ex: "  Vaga 3"
            vagas_livres.append(v)  # Adiciona à lista de vagas livres

    # Se não há vagas livres, avisa e encerra a função
    # "not vagas_livres" é True quando a lista está vazia
    if not vagas_livres:
        print("\n Não há vagas disponíveis!")
        return  # return sem valor = encerra a função aqui (sai sem fazer mais nada)

    # Solicita ao usuário o número da vaga desejada
    # .strip() remove espaços em branco no início e fim da string
    numero_vaga = input("\nEscolha o número da vaga: ").strip()

    # Procura a vaga escolhida na lista completa de vagas
    vaga_selecionada = None  # Inicializa como None (nenhuma vaga selecionada ainda)

    # Percorre todas as vagas para encontrar a que o usuário escolheu
    for v in vagas:
        # Verifica DUAS condições ao mesmo tempo:
        # 1. O número da vaga é o que o usuário digitou?
        # 2. A vaga ainda está livre? (prevenção contra dados desatualizados)
        if v["vaga"] == numero_vaga and v["estado"] == "livre":
            vaga_selecionada = v  # Guarda a referência à vaga encontrada
            break  # Sai do loop — não precisa continuar procurando

    # Se não encontrou a vaga (None), é porque era inválida ou já estava ocupada
    if not vaga_selecionada:
        print(" Vaga inválida ou já está ocupada!")
        return  # Encerra a função

    # Solicita a placa do veículo
    # .upper() converte para MAIÚSCULAS (ex: "abc-1234" → "ABC-1234")
    # .strip() remove espaços extras
    placa = input("Digite a placa do veículo (ex: ABC-1234): ").strip().upper()

    # Validação: placa não pode ser vazia
    if placa == "":
        print("Placa inválida")
        return

    # Verifica se a placa já está em alguma vaga ocupada
    # (impede que o mesmo carro ocupe duas vagas simultaneamente)
    for v in vagas:
        if v["placa"] == placa and v["estado"] == "ocupado":
            print(f" Veículo com placa {placa} já está estacionado na vaga {v['vaga']}!")
            return  # Encerra — não pode registrar a mesma placa duas vezes

    # Registra a entrada:
    # datetime.now() pega a data e hora ATUAL do computador
    # .strftime("%d/%m/%Y %H:%M") formata como string legível:
    #   %d = dia (01-31)    %m = mês (01-12)    %Y = ano (4 dígitos)
    #   %H = hora (00-23)   %M = minuto (00-59)
    # Exemplo: "06/07/2026 14:30"
    hora_entrada = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Atualiza os dados da vaga selecionada no dicionário
    # Como vaga_selecionada é uma REFERÊNCIA ao dicionário dentro da lista vagas,
    # modificar vaga_selecionada também modifica o item dentro da lista vagas
    vaga_selecionada["estado"] = "ocupado"    # Muda o estado de "livre" para "ocupado"
    vaga_selecionada["placa"] = placa         # Registra a placa do veículo
    vaga_selecionada["entrada"] = hora_entrada  # Registra o horário de entrada

    # Salva todas as vagas (com a modificação) de volta no arquivo CSV
    salvar_vagas(vagas)

    # Confirma o registro para o usuário
    print(f"\n Entrada registrada com sucesso!")
    print(f"  Vaga: {vaga_selecionada['vaga']}")
    print(f"  Placa: {placa}")
    print(f"  Hora de entrada: {hora_entrada}")


# ============================================================
# PARTE 4: REGISTRO DE SAÍDA
# ============================================================
# Registra a saída de um veículo: escolhe vaga ocupada, calcula
# tempo de permanência e valor a pagar, salva no histórico.
# ============================================================


def registrar_saida():
    """Registra a saída de um veículo e calcula o valor a pagar."""

    # Lê todas as vagas do arquivo CSV
    vagas = ler_vagas()

    print("\n--- REGISTRAR SAÍDA ---")

    # Mostra apenas as vagas que estão ocupadas (com veículos estacionados)
    print("\nVeículos estacionados:")
    vagas_ocupadas = []  # Lista para armazenar apenas vagas ocupadas

    for v in vagas:
        if v["estado"] == "ocupado":  # Filtra só as vagas com carro
            print(f"  Vaga {v['vaga']} - Placa {v['placa']}")  # Ex: "  Vaga 2 - Placa ABC-1234"
            vagas_ocupadas.append(v)

    # Se não há veículos estacionados, avisa e encerra
    if not vagas_ocupadas:
        print("\n Não há veículos estacionados!")
        return

    # Solicita o número da vaga que o veículo vai deixar
    numero_vaga = input("\nDigite o número da vaga: ").strip()

    # Procura a vaga escolhida (mesma lógica da função de entrada)
    vaga_selecionada = None

    for v in vagas:
        if v["vaga"] == numero_vaga and v["estado"] == "ocupado":
            vaga_selecionada = v
            break

    # Se não encontrou, a vaga é inválida ou já está livre
    if not vaga_selecionada:
        print(" Vaga inválida ou não está ocupada!")
        return

    # Registra o horário de saída (data e hora atual)
    hora_saida = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Pega o horário de entrada que estava salvo na vaga
    hora_entrada_str = vaga_selecionada["entrada"]  # Ex: "06/07/2026 14:30"

    # Calcula o tempo de permanência e o valor a pagar
    # A função retorna dois valores: horas e valor
    horas, valor = calcular_valor(hora_entrada_str, hora_saida)

    # Verifica se houve erro no cálculo (retornou None)
    # "is None" verifica se a variável é exatamente None
    if horas is None or valor is None:
        print(" Erro no horário de entrada/saída!")
        return

    # Salva a saída no arquivo de histórico
    # Modo "a" = append (adicionar ao final, sem apagar o que já existe)
    # Escreve no formato: placa;hora_entrada;hora_saida;valor
    # Exemplo: ABC-1234;06/07/2026 14:30;06/07/2026 17:30;15.00
    with open("historico_saida.csv", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{vaga_selecionada['placa']};{hora_entrada_str};{hora_saida};{valor:.2f}\n")
        # :.2f formata o valor com 2 casas decimais: 15.00

    # Libera a vaga — volta ao estado inicial
    vaga_selecionada["estado"] = "livre"    # Vaga fica disponível novamente
    vaga_selecionada["placa"] = "none"      # Remove a placa
    vaga_selecionada["entrada"] = "none"    # Remove o horário de entrada
    vaga_selecionada["saida"] = "none"      # Remove o horário de saída

    # Salva as alterações no arquivo CSV
    salvar_vagas(vagas)

    # Exibe o comprovante de saída
    print(f"\n✓ Saída registrada com sucesso!")
    print(f"  Vaga: {vaga_selecionada['vaga']}")
    print(f"  Placa: {vaga_selecionada['placa']}")
    print(f"  Hora de entrada: {hora_entrada_str}")
    print(f"  Hora de saída: {hora_saida}")
    print(f"  Tempo de permanência: {int(horas)} hora(s)")  # int() remove os decimais
    print(f"  Valor a pagar: R$ {valor:.2f}")  # Ex: R$ 15.00


def calcular_valor(hora_entrada_str, hora_saida):
    """Calcula o tempo de permanência e o valor a pagar.
    
    Regras:
    - Mínimo cobrado: 1 hora (mesmo que fique menos tempo)
    - Valor: R$ 5,00 por hora
    - Se o horário de saída for anterior ao de entrada, retorna erro
    """

    # Formato esperado das strings de data/hora
    formato = "%d/%m/%Y %H:%M"

    # strptime() = STRING PARSE TIME → converte string em objeto datetime
    # Converte a string "06/07/2026 14:30" em um objeto que Python entende como data
    entrada_dt = datetime.strptime(hora_entrada_str, formato)
    saida_dt = datetime.strptime(hora_saida, formato)

    # Calcula a diferença entre saída e entrada (objeto timedelta)
    # Exemplo: saida(17:30) - entrada(14:30) = 3 horas
    diferenca = saida_dt - entrada_dt

    # total_seconds() converte a diferença para segundos totais
    # Divide por 3600 (segundos em 1 hora) para obter o resultado em horas
    # Exemplo: 10800 segundos / 3600 = 3.0 horas
    horas = diferenca.total_seconds() / 3600

    # Se a saída foi ANTES da entrada (erro de dados), retorna None para indicar erro
    if horas <= 0:
        return None, None  # Retorna dois Nones (desempacotamento na função chamadora)

    # Regra de negócio: mínimo de 1 hora
    # Se ficou menos de 1 hora (ex: 0.5 horas = 30 minutos), cobra 1 hora
    if horas < 1:
        horas = 1

    # Calcula o valor: horas × R$ 5,00 por hora
    # Exemplo: 3 horas × 5.00 = R$ 15,00
    valor = horas * 5.00

    # Retorna os dois valores (a função chamadora faz: horas, valor = calcular_valor(...))
    return horas, valor


# ============================================================
# PARTE 5: RELATÓRIOS
# ============================================================
# Funções que geram relatórios sobre o estacionamento:
# - Veículos estacionados no momento
# - Faturamento (mensal, semanal e total)
# ============================================================


def relatorio_de_veiculos():
    """Mostra todos os veículos que estão estacionados no momento."""

    # Lê as vagas do arquivo
    vagas = ler_vagas()

    print("\n --- Veículos Estacionados --- \n")

    # Variável de controle para saber se há pelo menos um carro
    tem_carro = False  # Começa como False (assumindo que não há carros)

    # Percorre todas as vagas
    for v in vagas:
        if v["estado"] == "ocupado":  # Se a vaga está ocupada
            # Ex: "Vaga: 2 | Placa ABC-1234 | Hora de entrada 06/07/2026 14:30"
            print(f"Vaga: {v['vaga']} | Placa {v['placa']} | Hora de entrada {v['entrada']}")
            tem_carro = True  # Pelo menos um carro foi encontrado

    # Se após o loop tem_carro continua False, não há veículos
    if not tem_carro:
        print("\n Não há veículos estacionados no momento ")


def relatorio_faturamento():
    """Gera um relatório de faturamento mensal, semanal e total,
    lendo o arquivo historico_saida.csv e salvando em relatorio_do_faturamento.csv."""

    # Verifica se o arquivo de histórico existe antes de tentar ler
    # Se não existe, significa que nunca houve nenhuma saída registrada
    if not os.path.exists("historico_saida.csv"):
        print("\n Histórico de faturamento vazio!\n")
        return  # Encerra a função

    # Dicionários para acumular o faturamento por mês e por semana
    # Chave = identificador do mês/semana, Valor = soma dos valores pagos
    faturamento_mensal = {}   # Ex: {"072026": 75.00}
    faturamento_semanal = {}  # Ex: {"Semana 27 de 2026": 45.00}
    fatura_geral = 0.0        # Acumulador do total geral (começa em zero)

    # Abre o arquivo de histórico para leitura
    with open("historico_saida.csv", "r", encoding="utf-8") as arquivo:

        # Percorre cada linha do arquivo
        for linha in arquivo:
            # Cada linha tem o formato: placa;hora_entrada;hora_saida;valor
            # .strip() remove espaços e o \n do final da linha
            # .split(";") separa a linha em uma lista pelos ponto-e-vírgula
            # Exemplo: "ABC-1234;06/07/2026 14:30;06/07/2026 17:30;15.00"
            #          → ["ABC-1234", "06/07/2026 14:30", "06/07/2026 17:30", "15.00"]
            dados = linha.strip().split(";")

            # Validação: se a linha tem menos de 2 campos, está incompleta → pula
            if len(dados) < 2:
                continue  # Pula para a próxima linha do loop

            # Extrai os dados da linha
            # ATENÇÃO: aqui os índices parecem estar com problema no código original.
            # O arquivo grava: placa;entrada;saída;valor (índices 0,1,2,3)
            # Mas o código lê hora_da_saida no índice 0 e valor_pago no índice 1.
            # Isso funciona apenas se o historico_saida.csv tiver um formato diferente.
            hora_da_saida = dados[0]           # Primeiro campo
            valor_pago = float(dados[1])       # Segundo campo, convertido para float (decimal)

            # Converte a string de data/hora em um objeto datetime
            # Para extrair informações como mês e semana
            data_saida = datetime.strptime(hora_da_saida, "%d/%m/%Y %H:%M")

            # Extrai o identificador do mês no formato "MMYYYY" (mês + ano)
            # strftime("%m%Y") → Ex: "072026" (julho de 2026)
            mes = data_saida.strftime("%m%Y")

            # Extrai o identificador da semana no formato "Semana NN de YYYY"
            # %U = número da semana no ano (00-53, semanas começam no domingo)
            # Ex: "Semana 27 de 2026"
            semana = data_saida.strftime("Semana %U de %Y")

            # --- Faturamento mensal ---
            # Se o mês ainda não está no dicionário, inicializa com 0.0
            if mes not in faturamento_mensal:
                faturamento_mensal[mes] = 0.0
            # Soma o valor pago ao acumulador do mês
            faturamento_mensal[mes] += valor_pago

            # --- Faturamento semanal ---
            # Mesma lógica: inicializa se não existe, depois soma
            if semana not in faturamento_semanal:
                faturamento_semanal[semana] = 0.0
            faturamento_semanal[semana] += valor_pago

            # --- Faturamento geral ---
            # Acumula o valor no total geral
            fatura_geral += valor_pago

    # agora gera o arquivo de relatório
    # abre no modo escrita ("w") — cria ou sobrescreve o arquivo
    with open("relatorio_do_faturamento.csv", "w", encoding="utf-8") as faturamento:

        # Escreve o título do relatório
        faturamento.write("RELATORIO DE FATURAMENTO\n\n")

        # Escreve o faturamento por mês
        faturamento.write(" Faturamento por Mes: \n")
        for m in faturamento_mensal:
            # Para cada mês, escreve: identificador + valor formatado com 2 decimais
            # :.2f = formato com 2 casas decimais (ex: 75.00)
            faturamento.write(f" {m}: R$ {faturamento_mensal[m]:.2f} \n ")

        # Escreve o faturamento por semana
        faturamento.write("\n Faturamento semanal: \n")
        for s in faturamento_semanal:
            faturamento.write(f" {s}: R$ {faturamento_semanal[s]:.2f} \n")

        # Escreve o faturamento total
        faturamento.write(f"\n Faturamento total: R$ {fatura_geral:.2f}\n")

    # Lê e exibe o relatório na tela
    try:
        arquivo = open("relatorio_do_faturamento.csv")  # Abre o arquivo recém-criado
        print(arquivo.read())  # Lê todo o conteúdo e imprime na tela
    except FileNotFoundError:
        print("Arquivo não encontrado.")


# ============================================================
# PARTE 6: MENU PRINCIPAL (versão terminal/console)
# ============================================================
# Menu interativo para o usuário escolher as opções no terminal.
# NOTA: Este menu é duplicado pela função main() abaixo.
# A interface gráfica (Parte 8) substitui este menu.
# ============================================================


def menu():
    """Exibe o menu de opções e executa a função correspondente à escolha do usuário."""

    # Loop infinito — o menu continua aparecendo até o usuário escolher "Sair"
    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE ESTACIONAMENTO ===")
        print("1. Criar vagas iniciais")
        print("2. Registrar entrada de veículo")
        print("3. Registrar saída de veículo")
        print("4. Relatório de veículos estacionados")
        print("5. Relatório de faturamento")
        print("6. Sair")

        # Lê a opção do usuário
        # .strip() remove espaços em branco nas bordas
        opcao = input("Escolha uma opção: ").strip()

        # Verifica qual opção foi escolhida e chama a função correspondente
        # if/elif encadeado — só UMA opção será executada
        if opcao == "1":
            criar_vagas_iniciais()       # Cria as vagas no arquivo CSV
        elif opcao == "2":
            registrar_entrada()          # Registra a entrada de um veículo
        elif opcao == "3":
            registrar_saida()            # Registra a saída e calcula valor
        elif opcao == "4":
            relatorio_de_veiculos()      # Mostra veículos estacionados
        elif opcao == "5":
            relatorio_faturamento()      # Gera relatório de faturamento
        elif opcao == "6":
            print("Saindo do sistema...")
            break  # Sai do loop while, encerrando o menu
        else:
            # Qualquer opção que não seja 1-6 é inválida
            print("Opção inválida! Tente novamente.")


# ============================================================
# PARTE 7: PROGRAMA PRINCIPAL (versão terminal)
# ============================================================
# Função main() que combina o menu com funcionalidades extras.
# NOTA: Está comentada porque a interface gráfica (Parte 8) a substituiu.
# OBSERVAÇÃO: Há um problema neste código — ele chama menu() dentro
# do loop e depois pede opção novamente, causando duplicação.
# ============================================================


def main():
    """Função principal do programa (versão terminal). Atualmente desativada
    porque o programa é iniciado pela interface gráfica (Parte 8)."""

    print("Bem-vindo ao Sistema de Gerenciamento de Estacionamento!")

    # Loop principal do programa
    while True:
        menu()  # Exibe o menu e executa a opção escolhida
        # ⚠️ NOTA: Após menu() retornar (opção 6), o código abaixo
        # tenta ler outra opção, criando uma duplicação com o menu interno.

        opção = input("Selecione uma opção: ").strip()

        # Segundo conjunto de opções (duplicado do menu)
        if opção == "1":
            criar_vagas_iniciais()
        elif opção == "2":
            registrar_entrada()
            # Após registrar entrada, mostra o estado de todas as vagas
            vagas = ler_vagas()
            print("\nVagas do estacionamento:")
            for v in vagas:
                # Operador ternário: "Ocupada" se estado for "ocupado", senão "Livre"
                estado = "Ocupada" if v["estado"] == "ocupado" else "Livre"
                print(f"  Vaga {v['vaga']}: {estado}")
        elif opção == "3":
            registrar_saida()
        elif opção == "4":
            relatorio_de_veiculos()
        elif opção == "5":
            relatorio_faturamento()
        elif opção == "6":
            print("Saindo do sistema...")
            break  # Sai do loop while
        else:
            print("Opção inválida! Tente novamente.")

        # Pausa para o usuário ler o resultado antes de voltar ao menu
        input("\nPressione Enter para continuar...")


# main() comentado porque agora o programa é iniciado pela interface gráfica, criada na PARTE 8.
# main()


# ============================================================
# PARTE 8: INTERFACE GRÁFICA (TKINTER)
# ============================================================
# Tkinter é a biblioteca padrão do Python para criar interfaces gráficas.
# Principais componentes usados:
# - Tk()          → janela principal
# - Toplevel()    → janela secundária (filha da principal)
# - Label         → texto exibido na tela
# - Button        → botão clicável
# - Entry         → campo de digitação (input)
# - Listbox       → lista de itens selecionáveis
# - Text          → área de texto multilinha
# - Frame         → container para organizar outros widgets
# - ttk.Treeview  → tabela com colunas e linhas
# - Scrollbar     → barra de rolagem
# ============================================================


from tkinter import *        # Importa todos os componentes do Tkinter
from tkinter import ttk      # Importa componentes modernos (themed) do Tkinter


def atualizar_tabela():
    """Atualiza a tabela de vagas exibida na janela principal.
    Limpa todos os dados atuais e reinsere com os dados mais recentes do CSV."""

    # Limpa todos os itens existentes na tabela
    # tabela.get_children() retorna todos os IDs das linhas da tabela
    # tabela.delete(item) remove uma linha específica
    for item in tabela.get_children():
        tabela.delete(item)

    # Lê as vagas mais recentes do arquivo CSV
    vagas = ler_vagas()

    # Para cada vaga, insere uma nova linha na tabela
    for v in vagas:
        # Adiciona emoji para indicar visualmente o estado da vaga
        # 🟢 = verde (livre) | 🔴 = vermelho (ocupado)
        estado = "🟢 Livre" if v["estado"] == "livre" else "🔴 Ocupado"

        # Se a placa/entrada/saída for "none", exibe "---" (mais amigável)
        placa = v["placa"] if v["placa"] != "none" else "---"
        entrada = v["entrada"] if v["entrada"] != "none" else "---"
        saida = v["saida"] if v["saida"] != "none" else "---"

        # Insere uma nova linha na tabela
        # "" = item pai (vazio = nível raiz)
        # END = insere no final da tabela
        # values=() = valores de cada coluna na ordem definida
        tabela.insert("", END, values=(v["vaga"], estado, placa, entrada, saida))


# --- Tela: Criar vagas iniciais ---

def tela_criar_vagas():
    """Abre uma janela para o usuário criar as vagas do estacionamento."""

    # Toplevel() cria uma NOVA janela (filha da janela principal)
    # Diferente de Tk(), não cria uma nova aplicação — é uma janela auxiliar
    janela = Toplevel(janela_principal)
    janela.title("Criar Vagas")        # Título da janela
    janela.geometry('300x150')          # Largura × Altura em pixels

    # Label = rótulo — exibe um texto na tela
    # pack() posiciona o widget na janela (empacota)
    Label(janela, text="Quantidade de vagas:").pack()

    # Entry = campo de entrada de texto (onde o usuário digita)
    entrada_quantidade = Entry(janela)
    entrada_quantidade.pack()

    # Label vazio que será usado para mostrar mensagens de feedback
    label_mensagem = Label(janela, text="")
    label_mensagem.pack()

    # Função interna (aninhada) que é chamada quando o usuário clica em "Criar"
    # Funções internas podem acessar variáveis da função externa (closure)
    def confirmar():
        # .get() obtém o texto digitado no campo de entrada
        # .strip() remove espaços nas bordas
        qtd = entrada_quantidade.get().strip()

        # Validação: verifica se o que foi digitado é um número
        # .isdigit() retorna True se a string contém apenas dígitos (0-9)
        # Ex: "10" → True | "abc" → False | "5.5" → False
        if not qtd.isdigit():
            label_mensagem.config(text="Digite um número válido!")  # Atualiza o texto do label
            return  # Encerra a função sem fazer nada

        # Converte a string para inteiro
        qvagas = int(qtd)

        # Cria a estrutura de dados (mesma lógica da função criar_vagas_iniciais)
        lista = [["vaga", "estado", "placa", "entrada", "saida"]]  # Cabeçalho
        for i in range(qvagas):
            indice = str(i + 1)
            lista += [[indice, "livre", "none", "none", "none"]]

        # Escreve no arquivo CSV (mesma lógica da Parte 1)
        arquivo = open("vagas.csv", "w", newline="")
        csv_dados = csv.writer(arquivo, delimiter=";")
        for elemento in lista:
            csv_dados.writerow(elemento)
        arquivo.close()

        # Atualiza a tabela na janela principal com as novas vagas
        atualizar_tabela()

        # Mostra mensagem de sucesso
        label_mensagem.config(text=str(qvagas) + " vagas criadas com sucesso!")

    # Frame = container para organizar widgets (como uma caixa invisível)
    frame_botoes = Frame(janela)
    frame_botoes.pack(pady=5)  # pady=5 adiciona 5 pixels de espaçamento vertical

    # Button = botão clicável
    # text = texto exibido no botão
    # command = função a ser chamada quando clicado
    # side=LEFT posiciona os botões lado a lado (da esquerda para direita)
    # padx=5 adiciona 5 pixels de espaçamento horizontal entre os botões
    Button(frame_botoes, text="Criar", command=confirmar).pack(side=LEFT, padx=5)
    # janela.destroy fecha esta janela secundária (sem fechar a principal)
    Button(frame_botoes, text="Sair", command=janela.destroy).pack(side=LEFT, padx=5)


# --- Tela: Registrar entrada de veículo ---

def tela_registrar_entrada():
    """Abre uma janela para registrar a entrada de um veículo."""

    janela = Toplevel(janela_principal)
    janela.title("Registrar Entrada")
    janela.geometry('300x300')

    # Label indicando que abaixo haverá a lista de vagas livres
    Label(janela, text="Vagas livres:").pack()

    # Listbox = caixa de lista onde o usuário pode selecionar um item
    lista_vagas = Listbox(janela)
    lista_vagas.pack()

    # Preenche a Listbox com as vagas que estão livres
    vagas = ler_vagas()
    for v in vagas:
        if v["estado"] == "livre":
            # INSERT no END = insere o número da vaga no final da lista
            lista_vagas.insert(END, v["vaga"])  # Ex: "1", "3", "5"

    # Label e campo para digitar a placa
    Label(janela, text="Digite a placa do veículo (ex: ABC-1234):").pack()
    entrada_placa = Entry(janela)
    entrada_placa.pack()

    # Label para mensagens de feedback
    label_mensagem = Label(janela, text="")
    label_mensagem.pack()

    # Função chamada ao clicar em "Registrar"
    def confirmar():
        # curselection() retorna uma tupla com os índices dos itens selecionados
        # Ex: (2,) significa que o 3º item foi selecionado (índice começa em 0)
        selecao = lista_vagas.curselection()

        # Obtém a placa digitada, remove espaços e converte para maiúsculas
        placa = entrada_placa.get().strip().upper()

        # Validação: usuário deve selecionar uma vaga na lista
        if not selecao:  # Tupla vazia = nada selecionado
            label_mensagem.config(text="Selecione uma vaga!")
            return

        # Validação: placa não pode ser vazia
        if placa == "":
            label_mensagem.config(text="Digite a placa!")
            return

        # Pega o texto do item selecionado na Listbox
        # selecao[0] = índice do item selecionado
        # lista_vagas.get(índice) = texto do item naquele índice
        numero_vaga = lista_vagas.get(selecao[0])  # Ex: "3"

        # Relê as vagas do arquivo (para garantir dados atualizados)
        vagas = ler_vagas()

        # Verifica se a placa já está estacionada em outra vaga
        for v in vagas:
            if v["placa"] == placa and v["estado"] == "ocupado":
                label_mensagem.config(text="Essa placa já está na vaga " + v["vaga"])
                return

        # Procura a vaga selecionada e verifica se está livre
        vaga_selecionada = None
        for v in vagas:
            if v["vaga"] == numero_vaga and v["estado"] == "livre":
                vaga_selecionada = v
                break

        if vaga_selecionada is None:
            label_mensagem.config(text="Vaga inválida!")
            return

        # Registra a entrada (mesma lógica da versão terminal)
        hora_entrada = datetime.now().strftime("%d/%m/%Y %H:%M")
        vaga_selecionada["estado"] = "ocupado"
        vaga_selecionada["placa"] = placa
        vaga_selecionada["entrada"] = hora_entrada

        # Salva no CSV
        salvar_vagas(vagas)

        # Atualiza a tabela na janela principal
        atualizar_tabela()

        # Mensagem de sucesso
        label_mensagem.config(text="Entrada registrada na vaga " + numero_vaga)

    # Botões de ação
    frame_botoes = Frame(janela)
    frame_botoes.pack(pady=5)
    Button(frame_botoes, text="Registrar", command=confirmar).pack(side=LEFT, padx=5)
    Button(frame_botoes, text="Sair", command=janela.destroy).pack(side=LEFT, padx=5)


# --- Tela: Registrar saída de veículo ---

def tela_registrar_saida():
    """Abre uma janela para registrar a saída de um veículo e calcular o valor."""

    janela = Toplevel(janela_principal)
    janela.title("Registrar Saída")
    janela.geometry('300x270')

    Label(janela, text="Veículos estacionados:").pack()

    # Listbox com as vagas ocupadas
    lista_vagas = Listbox(janela)
    lista_vagas.pack()

    # Preenche a lista com vagas ocupadas (mostrando vaga + placa)
    vagas = ler_vagas()
    for v in vagas:
        if v["estado"] == "ocupado":
            lista_vagas.insert(END, v["vaga"] + " - " + v["placa"])  # Ex: "2 - ABC-1234"

    # Label para mensagens de feedback
    label_mensagem = Label(janela, text="")
    label_mensagem.pack()

    # Função chamada ao clicar em "Registrar"
    def confirmar():
        selecao = lista_vagas.curselection()

        if not selecao:
            label_mensagem.config(text="Selecione uma vaga!")
            return

        # Pega o texto do item selecionado e extrai o número da vaga
        # Texto no formato: "2 - ABC-1234"
        # .split(" - ") divide em: ["2", "ABC-1234"]
        # [0] pega o primeiro elemento = número da vaga
        texto = lista_vagas.get(selecao[0])
        numero_vaga = texto.split(" - ")[0]  # "2"

        # Relê as vagas do arquivo
        vagas = ler_vagas()

        # Procura a vaga selecionada
        vaga_selecionada = None
        for v in vagas:
            if v["vaga"] == numero_vaga and v["estado"] == "ocupado":
                vaga_selecionada = v
                break

        if vaga_selecionada is None:
            label_mensagem.config(text="Vaga inválida!")
            return

        # Registra o horário de saída
        hora_saida = datetime.now().strftime("%d/%m/%Y %H:%M")
        hora_entrada_str = vaga_selecionada["entrada"]

        # Converte as strings de data/hora em objetos datetime para cálculo
        formato = "%d/%m/%Y %H:%M"
        entrada_dt = datetime.strptime(hora_entrada_str, formato)
        saida_dt = datetime.strptime(hora_saida, formato)

        # Calcula a diferença de tempo
        diferenca = saida_dt - entrada_dt
        # total_seconds() → segundos totais da diferença
        # / 3600 → converte segundos para horas
        horas = diferenca.total_seconds() / 3600

        # Validação: saída não pode ser antes da entrada
        if horas <= 0:
            print("Erro no horário")
            return

        # Mínimo de 1 hora (mesma regra da função calcular_valor)
        if horas < 1:
            horas = 1

        # Calcula o valor: R$ 5,00 por hora
        valor = horas * 5.00

        # Salva no histórico de saídas (modo "a" = append, adiciona ao final)
        with open("historico_saida.csv", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{vaga_selecionada['placa']};{hora_entrada_str};{hora_saida};{valor:.2f}\n")

        # Libera a vaga
        vaga_selecionada["estado"] = "livre"
        vaga_selecionada["saida"] = hora_saida
        # NOTA: Aqui NÃO limpa a placa e entrada como na versão terminal.
        # Isso pode ser um bug — na versão terminal, placa e entrada voltam para "none".

        # Salva as alterações no CSV
        salvar_vagas(vagas)

        # Atualiza a tabela na janela principal
        atualizar_tabela()

        # Monta a mensagem de confirmação com quebras de linha (\n)
        texto_msg = "Saída registrada!\n"
        texto_msg += "Vaga: " + numero_vaga + "\n"
        texto_msg += "Tempo: " + str(int(horas)) + " hora(s)\n"
        texto_msg += "Valor a pagar: R$ " + str(round(valor, 2))
        # round(valor, 2) arredonda para 2 casas decimais

        label_mensagem.config(text=texto_msg)

    # Botões
    frame_botoes = Frame(janela)
    frame_botoes.pack(pady=5)
    Button(frame_botoes, text="Registrar", command=confirmar).pack(side=LEFT, padx=5)
    Button(frame_botoes, text="Sair", command=janela.destroy).pack(side=LEFT, padx=5)


# --- Tela: Relatório de veículos estacionados ---

def tela_relatorio_veiculos():
    """Abre uma janela mostrando todos os veículos estacionados no momento."""

    janela = Toplevel(janela_principal)
    janela.title("Veículos Estacionados")
    janela.geometry('500x200')

    # Listbox com largura de 70 caracteres para exibir os dados
    lista = Listbox(janela, width=70)
    lista.pack()

    vagas = ler_vagas()
    tem_carro = False

    # Percorre as vagas e mostra apenas as ocupadas
    for v in vagas:
        if v["estado"] == "ocupado":
            texto = "Vaga " + v["vaga"] + " | Placa " + v["placa"] + " | Entrada " + v["entrada"]
            lista.insert(END, texto)
            tem_carro = True

    # Se não há veículos, mostra mensagem
    if not tem_carro:
        lista.insert(END, "Não há veículos estacionados no momento.")

    # Botão de fechar
    frame_botao = Frame(janela)
    frame_botao.pack(pady=5)
    Button(frame_botao, text="Sair", command=janela.destroy).pack(padx=5)


# --- Tela: Relatório de faturamento ---

def tela_relatorio_faturamento():
    """Abre uma janela mostrando o relatório de faturamento."""

    janela = Toplevel(janela_principal)
    janela.title("Relatório de Faturamento")

    # Text = campo de texto multilinha (diferente de Entry que é linha única)
    # width=50 caracteres, height=20 linhas
    texto_caixa = Text(janela, width=50, height=20)
    texto_caixa.pack()

    # Verifica se existe histórico de saídas
    if not os.path.exists("historico_saida.csv"):
        texto_caixa.insert(END, "Histórico de faturamento vazio!")
        return

    # Reaproveita a função de relatório já criada na PARTE 5
    # Essa função gera o arquivo "relatorio_do_faturamento.csv"
    relatorio_faturamento()

    # Lê o arquivo gerado e exibe na caixa de texto
    with open("relatorio_do_faturamento.csv", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()          # Lê todo o conteúdo do arquivo
        texto_caixa.insert(END, conteudo)  # Insere na caixa de texto (END = no final)

    # Botão de fechar
    frame_botao = Frame(janela)
    frame_botao.pack(pady=5)
    Button(frame_botao, text="Sair", command=janela.destroy).pack(padx=5)


# ============================================================
# JANELA PRINCIPAL DA INTERFACE GRÁFICA
# ============================================================
# Aqui é construída a tela principal do aplicativo, com:
# - Título
# - Botões de navegação
# - Tabela de vagas com barra de rolagem
# - Botão de atualizar
# ============================================================


# Tk() cria a janela principal da aplicação (só pode haver UMA por programa)
janela_principal = Tk()
janela_principal.title("Sistema de Gerenciamento de Estacionamento")  # Título da barra de título
janela_principal.geometry('850x650')  # Largura: 850px, Altura: 650px
janela_principal.configure(bg="#34495e")  # bg = background (cor de fundo)
# #34495e é um código hexadecimal de cor (azul escuro acinzentado)

# --- Título do sistema ---
Label(
    janela_principal,           # Widget pai (onde o label será colocado)
    text="SISTEMA DE ESTACIONAMENTO",  # Texto exibido
    font=("Arial", 16, "bold"),  # Fonte: Arial, tamanho 16, negrito (bold)
    bg="#34495e",                # Cor de fundo do label (mesmo da janela para integrar)
    fg="white"                   # fg = foreground (cor do texto) — branco
).pack(pady=15)  # pady=15 adiciona 15 pixels de espaço acima e abaixo

# --- Botões do menu principal ---
# Cada Button chama a função correspondente à tela secundária
# width=35 define a largura do botão em caracteres
# pady=3 adiciona 3 pixels de espaço vertical entre os botões
Button(janela_principal, text="Criar vagas iniciais", command=tela_criar_vagas, width=35).pack(pady=3)
Button(janela_principal, text="Registrar entrada de veículo", command=tela_registrar_entrada, width=35).pack(pady=3)
Button(janela_principal, text="Registrar saída de veículo", command=tela_registrar_saida, width=35).pack(pady=3)
Button(janela_principal, text="Relatório de veículos estacionados", command=tela_relatorio_veiculos, width=35).pack(pady=3)
Button(janela_principal, text="Relatório de faturamento", command=tela_relatorio_faturamento, width=35).pack(pady=3)
Button(janela_principal, text="Sair", command=janela_principal.destroy, width=10).pack(pady=8)
# janela_principal.destroy fecha a janela principal, encerrando o programa
# width=10 — botão menor pois "Sair" é um texto curto

# --- Subtítulo da tabela ---
Label(
    janela_principal,
    text="VAGAS DO ESTACIONAMENTO",
    font=("Arial", 18, "bold"),  # Fonte maior que o título (18)
    bg="#34495e",
    fg="white"
).pack(pady=15)

# --- Frame que contém a tabela e a barra de rolagem ---
frame_tabela = Frame(janela_principal, bg="#34495e")
frame_tabela.pack(pady=10)

# --- Barra de rolagem vertical ---
# Scrollbar permite rolar o conteúdo quando há mais dados que o visível
scrollbar_y = Scrollbar(frame_tabela, orient=VERTICAL)  # orient=VERTICAL = barra na vertical
scrollbar_y.pack(side=RIGHT, fill=Y)  # side=RIGHT = posiciona à direita | fill=Y = preenche verticalmente

# --- Tabela (Treeview) ---
# ttk.Treeview é um widget que exibe dados em formato de tabela (linhas e colunas)
tabela = ttk.Treeview(
    frame_tabela,
    columns=("vaga", "estado", "placa", "entrada", "saida"),  # Nomes das colunas
    show="headings",   # Mostra apenas os cabeçalhos (sem coluna de ícones padrão)
    height=15,         # Quantidade de linhas visíveis
    yscrollcommand=scrollbar_y.set  # Conecta a barra de rolagem à tabela
)

# Configura a barra de rolagem para controlar a tabela
# yview = método que move a visão da tabela verticalmente
scrollbar_y.config(command=tabela.yview)

# Define o texto do cabeçalho de cada coluna
tabela.heading("vaga", text="Vaga")
tabela.heading("estado", text="Estado")
tabela.heading("placa", text="Placa")
tabela.heading("entrada", text="Entrada")
tabela.heading("saida", text="Saída")

# Configura a largura e o alinhamento de cada coluna
# width = largura em pixels | anchor=CENTER = texto centralizado
tabela.column("vaga", width=70, anchor=CENTER)
tabela.column("estado", width=130, anchor=CENTER)
tabela.column("placa", width=150, anchor=CENTER)
tabela.column("entrada", width=180, anchor=CENTER)
tabela.column("saida", width=180, anchor=CENTER)

# Posiciona a tabela no frame
# side=LEFT = à esquerda (da scrollbar)
# fill=BOTH = preenche horizontal e verticalmente
# expand=True = expande para ocupar espaço disponível
tabela.pack(side=LEFT, fill=BOTH, expand=True)

# Botão para atualizar a tabela manualmente
Button(janela_principal, text="Atualizar tabela", command=atualizar_tabela, width=20).pack(pady=8)

# Atualiza a tabela quando o programa inicia (carrega dados do CSV)
atualizar_tabela()

# mainloop() é o LOOP PRINCIPAL do Tkinter
# Ele mantém a janela aberta e "escuta" eventos (cliques, digitação, etc.)
# Sem mainloop(), a janela aparece e fecha imediatamente
# O programa fica "preso" nesta linha até a janela ser fechada
janela_principal.mainloop()
