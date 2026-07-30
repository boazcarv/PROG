"""Hierarquia de exceções do sistema (Tópico 3)."""


class ErroBiblioteca(Exception):
    """Classe-base: qualquer erro do sistema herda desta."""


class ItemIndisponivelError(ErroBiblioteca):
    def __init__(self, titulo):
        super().__init__(f"'{titulo}' já está emprestado.")


class ItemNaoEncontradoError(ErroBiblioteca):
    def __init__(self, codigo):
        super().__init__(f"Nenhum item com código {codigo}.")


class DadosInvalidosError(ErroBiblioteca):
    pass
