class EntregaInvalidaError(Exception):
    '''Erro lançado quando a entrega apresenta algum problema.'''
    pass

class EntregaDuplicadaError(Exception):
    '''Erro lançado quando duas entregas possuem o mesmo código, ficando duplicadas.'''
    pass