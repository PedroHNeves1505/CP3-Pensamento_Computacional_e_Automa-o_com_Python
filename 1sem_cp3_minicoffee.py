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
        
        nome_produto = ""
        preco_unitario = 0
        
        match codigo_compra:
            case '100':
                nome_produto = 'Expresso'
                preco_unitario = 5
            case '101': 
                nome_produto = 'Café com Leite'
                preco_unitario = 6
            case '102': 
                nome_produto = 'Pão de Queijo'
                preco_unitario = 7
            case '103': 
                nome_produto = 'Refrigerante'
                preco_unitario = 10
            case _:
                print('Item inexistente! Tente novamente')
                continue  

        if nome_produto in carrinho:
            indice = carrinho.index(nome_produto)
            
            qnt_comprados[indice] += qnt_compra
            subtotais[indice] += preco_unitario * qnt_compra
        else:
            carrinho.append(nome_produto)
            qnt_comprados.append(qnt_compra)
            subtotais.append(preco_unitario * qnt_compra)
            
        print('Item adicionado ao pedido\n\n\n')

produtos_comprados = ""
quantidade_produto = ""
subtotal_produtos = ""
valor_total = 0

for i in range(len(carrinho)):
    produtos_comprados += f'| {carrinho[i]}'.ljust(20)

for i in range(len(qnt_comprados)):
    quantidade_produto += f'| {qnt_comprados[i]}'.ljust(8)

for i in range(len(subtotais)):
    subtotal_produtos += f'| R$ {subtotais[i]:.2f} '

for i in range(len(subtotais)):
    valor_total += subtotais[i]

print('----Resumo Final----')
print(f'Cliente: {nome}')
print(f'Quantidade de letras: {qnt_letras}')
print(f'Primeira letra: {primeira_letra}')
print(f'Produtos comprados:         {produtos_comprados}')
print(f'Quantidade de cada produto: {quantidade_produto}')
print(f'Subtotalde cadaproduto:     {subtotal_produtos}')
print(f'Total do pedido: R${valor_total:.2f}')

print('\n\n\n----Mensagem Final----')
if valor_total >= 40:
    print('Cliente ganhou um brinde!')
elif valor_total >=25:
    print('Cliente ganhou um cupom para a próxima compra!')
else:
    print('Obrigado pela compra!')