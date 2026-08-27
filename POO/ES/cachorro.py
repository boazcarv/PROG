class cachorro:
    
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade if idade >= 0 else 0

    def __str__(self):
      
        return f"{self.nome} ({self.raca}) - {self.idade} anos"

    def latir(self):
     
        print(f"{self.nome} está latindo!")

    def comer(self):
     
        print(f"{self.nome} está comendo!")

    def dormir(self):
     
        print(f"{self.nome} está dormindo!")

    def brincar(self):
      
        print(f"{self.nome} está brincando!")

