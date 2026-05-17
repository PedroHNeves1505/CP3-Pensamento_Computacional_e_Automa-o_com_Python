# RM: 571382 - Pedro Henrique Neves
# RM: 572733 - Akin Alexandre Mendes Martin 
# RM: 570544 - Maria Eduarda Rocha Benjamin

nome = input('Digite seu nome: ')
qnt_letras = len(nome)
primeira_letra = nome[0]

cardapio = [
    ['100', 'Expresso', 5.0],
    ['101', 'Café com Leite', 6.0],
    ['102', 'Pão de Queijo', 7.0],
    ['103', 'Refigerante', 10.0],
]

def mostrar_cardapio(cardapio):
    print('----CARDÁPIO----'.center(35))
    print(f'{'CÓDIGO'.ljust(8)} | {'PRODUTO'.ljust(15)} | PREÇO')
    for array in cardapio:
        print(f'{array[0].ljust(8)} | {array[1].ljust(15)} | {array[2]}')


