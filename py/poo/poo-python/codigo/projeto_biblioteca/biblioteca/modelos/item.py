"""
Modelos do acervo (Tópicos 1 e 2).

Hierarquia:
    ItemAcervo (abstrata)
        ├── Livro
        └── DVD
"""

from abc import ABC, abstractmethod

from ..excecoes import DadosInvalidosError, ItemIndisponivelError


class ItemAcervo(ABC):
    """Classe ABSTRATA: define o contrato comum a todo item do acervo."""

    def __init__(self, codigo, titulo, ano):
        self.codigo = codigo
        self.titulo = titulo
        self.ano = ano                  # passa pelo setter (validação)
        self._emprestado = False        # ENCAPSULAMENTO (protegido)

    # ----- propriedade com validação -----
    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, valor):
        if not isinstance(valor, int) or valor < 1400:
            raise DadosInvalidosError(f"Ano inválido: {valor!r}")
        self.__ano = valor

    @property
    def emprestado(self):
        return self._emprestado

    # ----- métodos abstratos: cada filha implementa do seu jeito -----
    @abstractmethod
    def prazo_dias(self):
        """Quantos dias o item pode ficar emprestado."""

    @abstractmethod
    def descricao(self):
        """Texto descritivo específico do tipo de item."""

    # ----- comportamento comum -----
    def emprestar(self):
        if self._emprestado:
            raise ItemIndisponivelError(self.titulo)
        self._emprestado = True

    def devolver(self):
        self._emprestado = False

    # ----- serialização (Tópico 5) -----
    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "codigo": self.codigo,
            "titulo": self.titulo,
            "ano": self.ano,
            "emprestado": self._emprestado,
        }

    def __str__(self):
        status = "EMPRESTADO" if self._emprestado else "disponível"
        return f"[{self.codigo}] {self.descricao()} — {status}"


class Livro(ItemAcervo):
    def __init__(self, codigo, titulo, ano, autor, paginas, emprestado=False):
        super().__init__(codigo, titulo, ano)
        self.autor = autor
        self.paginas = paginas
        self._emprestado = emprestado

    def prazo_dias(self):
        return 14

    def descricao(self):
        return f"{self.titulo}, de {self.autor} ({self.ano}, {self.paginas}p)"

    def to_dict(self):
        d = super().to_dict()           # reaproveita o pai
        d.update(autor=self.autor, paginas=self.paginas)
        return d


class DVD(ItemAcervo):
    def __init__(self, codigo, titulo, ano, duracao_min, emprestado=False):
        super().__init__(codigo, titulo, ano)
        self.duracao_min = duracao_min
        self._emprestado = emprestado

    def prazo_dias(self):
        return 3                        # POLIMORFISMO: prazo diferente

    def descricao(self):
        return f"{self.titulo} ({self.ano}, {self.duracao_min} min)"

    def to_dict(self):
        d = super().to_dict()
        d.update(duracao_min=self.duracao_min)
        return d


# ----- fábrica: dicionário -> objeto do tipo certo -----
def item_from_dict(d):
    tipo = d.get("tipo")
    if tipo == "Livro":
        return Livro(d["codigo"], d["titulo"], d["ano"],
                     d["autor"], d["paginas"], d["emprestado"])
    if tipo == "DVD":
        return DVD(d["codigo"], d["titulo"], d["ano"],
                   d["duracao_min"], d["emprestado"])
    raise DadosInvalidosError(f"Tipo desconhecido: {tipo!r}")
