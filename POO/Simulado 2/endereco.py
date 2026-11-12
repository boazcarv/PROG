@dataclass
class Endereco:
    cep: str
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    complemento: str | None = None
    ponto_referencia: str | None = None

    def __str__(self) -> str:
        return(f"ENDEREÇO -> CEP: {self.cep} | Logradouro: {self.logradouro} | Número: {self.numero} | Bairro: {self.bairro} | Estado: {self.estado} | Complemento: {self.complemento} | Ponto de referência: {self.ponto_referencia}")

class Cliente:
    def __init__(self, nome: str, cpf: str, endereco: Endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"DADOS DO CLIENTE -> Nome: {self.nome} | CPF: {self.cpf} | Endereço: {self.endereco}")

    

