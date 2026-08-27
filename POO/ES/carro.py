class carro:
    def __init__(self, marca, modelo, ano, cor, velocidade_maxima):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} está ligado.")
    