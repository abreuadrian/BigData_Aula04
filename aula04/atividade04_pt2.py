#Atividade 02 ------------------------------------------------------------------------------------------------
price = float(input('Informe o preço da compra: '))
print('[1] - À vista\n[2] - Parcelado')
payment = int(input('Selecione a forma de pagamento: '))

if price > 250 and payment == 1:
    desc = price * 0.16
    new_price = price - desc
    print('\nSua compra foi maior que R$250,00.')
    print(f'Você ganhou 16% de desconto. Total a pagar R${new_price:.2f}.')
else: 
    print(f'Sua compra ficou em R${price:.2f}.')