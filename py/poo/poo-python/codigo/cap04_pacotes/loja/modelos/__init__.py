"""
Pacote 'modelos'.

O __init__.py transforma a pasta em pacote e permite reexportar nomes,
encurtando o import de quem for usar o pacote:

    from loja.modelos import Produto, Cliente
"""

from .produto import Produto
from .cliente import Cliente

__all__ = ["Produto", "Cliente"]
