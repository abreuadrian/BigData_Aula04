#Atividade04:
m_time = int(input('Informe o tempo de filiação: '))
v_move = float(input('Informe o valor movimentado (Últimos 6 meses): '))

if m_time > 3 or v_move > 5000:
    print('\nParabéns. Você tem direito ao benefício especial')
else: print('\nAinda não atende aos critérios mínimos')