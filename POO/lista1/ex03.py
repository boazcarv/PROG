# Exercício 03 - Estruturas sequenciais
# Lê hora e minuto e informa quantos minutos se passaram
# desde o início do dia.

hora = int(input('Digite a hora (0 a 23): '))
minuto = int(input('Digite o minuto (0 a 59): '))

minutos = hora * 60 + minuto
print(f'Passaram-se {minutos} minutos desde o início do dia.')
