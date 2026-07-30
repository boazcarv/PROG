"""
Serviço de acervo: regras de negócio + persistência em JSON
(Tópicos 3, 4 e 5).
"""

import json
from pathlib import Path

from ..excecoes import ItemNaoEncontradoError
from ..modelos import item_from_dict


class Acervo:
    """COMPOSIÇÃO: o Acervo TEM-UMA lista de ItemAcervo."""

    def __init__(self, caminho_arquivo="acervo.json"):
        self.caminho = Path(caminho_arquivo)
        self.itens = []

    # ---------- CRUD ----------
    def adicionar(self, item):
        self.itens.append(item)

    def buscar(self, codigo):
        for item in self.itens:
            if item.codigo == codigo:
                return item
        raise ItemNaoEncontradoError(codigo)

    def remover(self, codigo):
        self.itens.remove(self.buscar(codigo))

    def disponiveis(self):
        return [i for i in self.itens if not i.emprestado]

    def emprestados(self):
        return [i for i in self.itens if i.emprestado]

    # ---------- persistência ----------
    def salvar(self):
        dados = [item.to_dict() for item in self.itens]
        with open(self.caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)

    def carregar(self):
        if not self.caminho.exists():
            self.itens = []
            return self
        with open(self.caminho, encoding="utf-8") as f:
            self.itens = [item_from_dict(d) for d in json.load(f)]
        return self

    def __len__(self):
        return len(self.itens)

    def __iter__(self):
        return iter(self.itens)
