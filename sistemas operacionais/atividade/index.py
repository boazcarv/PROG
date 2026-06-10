"""Simulador simples de escalonamento FIFO/SJF."""


def ler_processos():
    print("SIMULADOR DE ESCALONAMENTO")
    print("Digite um tempo por linha. Aperte Enter vazio para terminar.\n")

    processos = []
    i = 1

    while True:
        entrada = input(f"P{i}: ").strip()
        if entrada == "":
            break

        try:
            burst = float(entrada)
            if burst < 0:
                print("Digite um valor positivo.")
                continue

            processos.append({"id": f"P{i}", "burst": burst, "ordem": i})
            i += 1
        except ValueError:
            print("Valor inválido.")

    return processos


def escolher_algoritmo(processos):
    while True:
        opcao = input("Escolha o algoritmo (1-FIFO, 2-SJF): ").strip()

        if opcao == "1":
            return processos
        if opcao == "2":
            return sorted(processos, key=lambda p: (p["burst"], p["ordem"]))

        print("Opção inválida.")


def calcular_e_exibir(processos):
    tempo = 0
    soma_turnaround = 0

    print("\nProcesso   Espera   Turnaround")

    for processo in processos:
        espera = tempo
        tempo += processo["burst"]
        turnaround = tempo
        soma_turnaround += turnaround

        print(f"{processo['id']:<10}{espera:<9.2f}{turnaround:.2f}")

    media = soma_turnaround / len(processos)
    print(f"\nMédia do turnaround: {media:.2f}")


def main():
    processos = ler_processos()

    if not processos:
        print("Nenhum processo informado.")
        return

    processos = escolher_algoritmo(processos)
    calcular_e_exibir(processos)


if __name__ == "__main__":
    main()
