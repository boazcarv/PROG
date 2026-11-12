"""
Avaliação 2 - Programação Orientada a Objetos - T6
Professor: Higor Morais

Demonstração completa do sistema de controle de entregas.
"""

from datetime import date

from endereco import Endereco
from cliente import Cliente
from veiculo import Moto, Caminhao, Veiculo
from entrega import Entrega
from controle import ControleEntregas
from exceptions import EntregaInvalidaError, EntregaDuplicadaError


def separador(titulo: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {titulo}")
    print(f"{'=' * 60}")


if __name__ == "__main__":

    separador("1. CADASTRO DE ENDEREÇOS E CLIENTES")

    end1: Endereco = Endereco(
        rua="Rua das Flores", numero=123, cidade="São Paulo", estado="SP", cep="01001-000"
    )
    end2: Endereco = Endereco(
        rua="Av. Brasil", numero=456, cidade="Rio de Janeiro", estado="RJ", cep="20040-020"
    )
    end3: Endereco = Endereco(
        rua="Rua XV de Novembro", numero=789, cidade="Curitiba", estado="PR", cep="80020-310"
    )

    cliente1: Cliente = Cliente(nome="Ana Silva", cpf="111.222.333-44", endereco=end1)
    cliente2: Cliente = Cliente(nome="Bruno Costa", cpf="555.666.777-88", endereco=end2)
    cliente3: Cliente = Cliente(nome="Carla Dias", cpf="999.000.111-22", endereco=end3)

    print(cliente1)
    print()
    print(cliente2)
    print()
    print(cliente3)

    separador("2. CADASTRO DE VEÍCULOS (HERANÇA)")

    moto1: Moto = Moto(placa="ABC-1234", modelo="Honda CG 160")
    caminhao1: Caminhao = Caminhao(placa="XYZ-9876", modelo="Volvo FH 540")
    moto2: Moto = Moto(placa="DEF-5678", modelo="Yamaha Fazer 250")

    print(moto1)
    print(caminhao1)
    print(moto2)

    separador("3. CADASTRO DE ENTREGAS (ENCAPSULAMENTO)")

    entrega1: Entrega = Entrega(
        codigo="ENT-001",
        data_prevista=date(2025, 7, 20),
        peso=5.0,
        valor_frete=200.00,
        cliente=cliente1,
        veiculo=moto1,
    )

    entrega2: Entrega = Entrega(
        codigo="ENT-002",
        data_prevista=date(2025, 7, 15),
        peso=1500.0,
        valor_frete=3500.00,
        cliente=cliente2,
        veiculo=caminhao1,
    )

    entrega3: Entrega = Entrega(
        codigo="ENT-003",
        data_prevista=date(2025, 7, 18),
        peso=2.5,
        valor_frete=150.00,
        cliente=cliente3,
        veiculo=moto2,
    )

    print("Entregas criadas com sucesso!")

    # -------------------------------------------------------
    # 4. Polimorfismo — cálculo de taxa por tipo de veículo
    # -------------------------------------------------------
    separador("4. POLIMORFISMO — CÁLCULO DE TAXA")

    veiculos_demo: list[Veiculo] = [moto1, caminhao1, moto2]
    frete_demo: float = 1000.00

    for v in veiculos_demo:
        taxa: float = v.calcular_taxa(frete_demo)
        print(f"  {v.modelo:20s} → taxa sobre R$ {frete_demo:.2f} = R$ {taxa:.2f}")

    print()
    print("Taxas aplicadas em cada entrega:")
    for ent in [entrega1, entrega2, entrega3]:
        print(
            f"  [{ent.codigo}] Frete R$ {ent.valor_frete:.2f} | "
            f"Veículo: {ent.veiculo.__class__.__name__:8s} | "
            f"Taxa: R$ {ent.calcular_taxa_veiculo():.2f}"
        )

    separador("5. CONTROLE DE ENTREGAS E EXCEÇÕES")

    controle: ControleEntregas = ControleEntregas()

    # Adicionando entregas válidas
    for ent in [entrega1, entrega2, entrega3]:
        try:
            controle.adicionar_entrega(ent)
            print(f"  ✔ Entrega '{ent.codigo}' cadastrada.")
        except (EntregaInvalidaError, EntregaDuplicadaError) as ex:
            print(f"  ✘ Erro: {ex}")

    # Tentativa de entrega duplicada
    print("\n  >> Tentando cadastrar entrega duplicada (ENT-001)...")
    try:
        entrega_dup: Entrega = Entrega(
            codigo="ENT-001",
            data_prevista=date(2025, 8, 1),
            peso=10.0,
            valor_frete=300.00,
            cliente=cliente1,
            veiculo=moto1,
        )
        controle.adicionar_entrega(entrega_dup)
    except EntregaDuplicadaError as ex:
        print(f"  ✘ EntregaDuplicadaError: {ex}")

    # Tentativa de entrega com peso inválido
    print("\n  >> Tentando criar entrega com peso negativo...")
    try:
        entrega_inv: Entrega = Entrega(
            codigo="ENT-099",
            data_prevista=date(2025, 8, 5),
            peso=-3.0,
            valor_frete=100.00,
            cliente=cliente2,
            veiculo=caminhao1,
        )
    except EntregaInvalidaError as ex:
        print(f"  ✘ EntregaInvalidaError: {ex}")

    # Tentativa de entrega com frete zero
    print("\n  >> Tentando criar entrega com frete zero...")
    try:
        entrega_inv2: Entrega = Entrega(
            codigo="ENT-098",
            data_prevista=date(2025, 8, 5),
            peso=10.0,
            valor_frete=0.0,
            cliente=cliente3,
            veiculo=moto2,
        )
    except EntregaInvalidaError as ex:
        print(f"  ✘ EntregaInvalidaError: {ex}")

    separador("6. LISTAGEM ORDENADA POR DATA PREVISTA")

    print(f"\n  Total de entregas cadastradas: {controle.total_entregas}\n")

    entregas_ordenadas = controle.listar_entregas_ordenadas_por_data()
    for i, ent in enumerate(entregas_ordenadas, start=1):
        print(f"  {i}ª — [{ent.codigo}] {ent.data_prevista.strftime('%d/%m/%Y')}")

    print("\n--- Detalhes completos (ordenados) ---\n")
    for ent in entregas_ordenadas:
        print(ent)
        print()

    separador("FIM DA DEMONSTRAÇÃO")