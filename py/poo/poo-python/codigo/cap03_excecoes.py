"""
Capítulo 3 - Tratamento de Exceções
Rode com:  python3 cap03_excecoes.py
"""

# ---------------------------------------------------------------
# 3.1 try / except / else / finally
# ---------------------------------------------------------------
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("  [except] Não dá para dividir por zero!")
        return None
    except TypeError as e:
        print(f"  [except] Tipos inválidos: {e}")
        return None
    else:
        print("  [else] Deu tudo certo.")
        return resultado
    finally:
        print("  [finally] Sempre executo, com erro ou sem erro.")


# ---------------------------------------------------------------
# 3.2 Criando exceções próprias (hierarquia)
# ---------------------------------------------------------------
class ErroBanco(Exception):
    """Classe-base de todos os erros do nosso banco."""


class SaldoInsuficienteError(ErroBanco):
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        super().__init__(
            f"Saldo insuficiente: você tem R$ {saldo:.2f} "
            f"e tentou sacar R$ {valor:.2f} (faltam R$ {valor - saldo:.2f})."
        )


class ValorInvalidoError(ErroBanco):
    pass


class Conta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def sacar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("O valor do saque deve ser positivo.")
        if valor > self.__saldo:
            raise SaldoInsuficienteError(self.__saldo, valor)
        self.__saldo -= valor
        return self.__saldo


# ---------------------------------------------------------------
# 3.3 Encadeamento (raise ... from) e context manager
# ---------------------------------------------------------------
class ErroDeLeitura(ErroBanco):
    pass


def ler_saldo_do_arquivo(caminho):
    try:
        with open(caminho, encoding="utf-8") as f:   # 'with' fecha sozinho
            return float(f.read())
    except FileNotFoundError as e:
        raise ErroDeLeitura(f"Arquivo '{caminho}' não existe.") from e
    except ValueError as e:
        raise ErroDeLeitura("Conteúdo do arquivo não é um número.") from e


# ---------------------------------------------------------------
# DEMONSTRAÇÃO
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("--- 3.1 try/except/else/finally ---")
    print("10 / 2 =", dividir(10, 2))
    print("10 / 0 =", dividir(10, 0))
    print('10 / "a" =', dividir(10, "a"))

    print("\n--- 3.2 Exceções personalizadas ---")
    conta = Conta("Ana", 500)
    for valor in [200, -5, 10_000]:
        try:
            novo = conta.sacar(valor)
            print(f"  Saque de R$ {valor:.2f} OK. Novo saldo: R$ {novo:.2f}")
        except ValorInvalidoError as e:
            print(f"  [ValorInvalido] {e}")
        except SaldoInsuficienteError as e:
            print(f"  [SaldoInsuficiente] {e}")
        except ErroBanco as e:                 # pega qualquer erro do banco
            print(f"  [ErroBanco genérico] {e}")

    print("\n--- 3.3 Encadeamento de exceções ---")
    try:
        ler_saldo_do_arquivo("nao_existe.txt")
    except ErroDeLeitura as e:
        print(f"  {e}")
        print(f"  Causa original: {type(e.__cause__).__name__}")
