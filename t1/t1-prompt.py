

# A função recebe a quantidade e o preço de um produto e retorna a o valor multiplicado 
def sum_price(qtd, price):
    return price * qtd

# Controla o loop    
hasProduct = True

# Controla o valor total
totalPrice = 0

# Enquanto o usuário desejar incluir novos produtos no valor total da compra
while(hasProduct):
    try:
        name = input('\nDigite o nome do produto:')
        qtd = int(input('Digite a quantidade do produto:'))
        price = float(input('Digite o preço do produto:'))

        totalPrice += sum_price(qtd, price)

        hasProduct = input('Incluir outro produto? (s/n)') == 's'


    except ValueError as ve:
        print('\nOcorreu um erro ao calcular o valor: ', ve)
        break

print('Total: $', totalPrice)