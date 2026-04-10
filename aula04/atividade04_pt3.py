#Atividade03:
stock = int(input('Informe a quantidade de caixas no estoque: '))
order = int(input('Informe a quantidade do pedido: '))
weight = float(input('Informe o peso total do pedido: '))

if stock >= order and weight <= 50:
    print('\nPedido liberado')
else: print('\nO pedido não pode ser enviado. Necessário revisar as condições.')