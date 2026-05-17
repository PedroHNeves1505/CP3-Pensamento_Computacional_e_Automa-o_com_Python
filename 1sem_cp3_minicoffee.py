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

def calcular_subtotal(preco, qnt):
    return preco * qnt

opicao = -1
carrinho = []        
qnt_comprados = []   
subtotais = []       

while opicao != 0:
    mostrar_cardapio(cardapio)
    print('\n\n')
    print('----MENU----'.center(35))
    print('1 - Adicionar produto ao carrinho')
    print('0 - Encerrar Compra')
    print(f"{'-' * 30}")
    opicao = int(input('Digite a opição desejada: '))

    if opicao == 1:
        codigo_compra = input('Digite o código do produto desejado: ')
        qnt_compra = int(input('Digite a quantidade desejada: '))
        
        match codigo_compra:
            case '100':
                carrinho.append('Expresso')
                qnt_comprados.append(qnt_compra)
                subtotais.append(calcular_subtotal(5, qnt_compra))
                print('Item adicionado ao pedido\n\n\n')
            case '101': 
                carrinho.append('Café com Leite')
                qnt_comprados.append(qnt_compra)
                subtotais.append(calcular_subtotal(6, qnt_compra))
                print('Item adicionado ao pedido\n\n\n')
            case '102': 
                carrinho.append('Pão de Queijo')
                qnt_comprados.append(qnt_compra)
                subtotais.append(calcular_subtotal(7, qnt_compra))
                print('Item adicionado ao pedido\n\n\n')
            case '103': 
                carrinho.append('Refrigerante')
                qnt_comprados.append(qnt_compra)
                subtotais.append(calcular_subtotal(10, qnt_compra))
                print('Item adicionado ao pedido\n\n\n')
            case _:
                print('Item inexistente! Tente novamente')
        print(f"{'=~' * 10}\n\n")
    else:
        continue
