print('=====EXERCICIO CONVERTENDO CELSIUS 14 MUNDO 1=======')
resposta = ' '
while resposta!='s':

    c = float(input('ENSIRA AQUI A TEMPERATURA EM °C: '))
    f = ( 9 * c / 5 ) + 32
    print('A TEMPERATURA EM °C: {0} E TEMPERATURA CONVERTIDA PARA °F: {1}'.format(c , f))
    resposta = input('DESEJA SAIR ? [s] PARA SIM E [n] PARA NÃO: ')
SystemExit('s')
