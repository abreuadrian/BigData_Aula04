#Estruturas de condição (if, elif, else)

#Ex01.:
time = input('Digite seu time: ').lower()

if time == 'flamengo':
    print('Você torce pro maior do RJ')

if time == 'nenhum':
    print('tsc...')

else: 
    print('Seu time nao é tão grande assim...')

#Ex02.:
idade = int(input('Informe sua idade: '))

if idade < 18:
    print('Você é menor de idade. Não pode entrar.')

else:
    print('Você é maior de idade. Pode entrar.')

#Ex03.:
points = int(input('Informe sua pontuação: '))

if points >= 100:
    print('Excelente!')
elif points >= 50:
    print('Bom desempenho!')
elif points >= 25:
    print('Satisfatório.')
else:
    print('Pratique mais')