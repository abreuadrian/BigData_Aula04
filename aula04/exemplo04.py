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

#-----------Operadores AND e OR-----------
    
#Ex04.:
user = input('Login: ')
password = input('Senha: ')

if user == 'admin' and password == '1234':
    print('Login efetuado com sucesso!')
else:
    print('Usuário ou senha incorreta.')

#Ex05.: if encadeado
nota = float(input('Informe sua nota: '))

if nota >= 9:
    print('A')
elif nota >= 7:
    print('B')
elif nota >= 5:
    print('C')
elif nota >= 2:
    print('D')
else:
    print('E')

#Ex06.: ifs não encadeados
nota = float(input('Informe sua nota: '))

if nota >= 9:
    print('A')

if nota >= 7:
    print('B')

if nota >= 5:
    print('C')

if nota >= 2:
    print('D')

else:
    print('E')

#Ex07.: ifs aninhados
nota = float(input('Informe sua nota: '))
freq = float(input('Informe a frequência: '))

if nota >= 7:
    if freq >= 75:
        print('Você foi aprovado!')
    else:
        print('Reprovado por falta')
else:
    print('Reprovado por nota')
    