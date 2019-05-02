import math

print('EXERCICIO NUMERO 15 ALUGUEl DE CARROS')
carro = int(input('QUANTOS DIAS VOCE FICOU COM O CARRO ?: '))
sair = ''
while (sair!='s'):
    km = float(input('QUANTOS KM FORAM RODADOS ?: '))
    pago = (carro * 60) + (km * 0.15)
    print('O TOTAL A SER PAGO É R$: {:.2f}'.format(pago))
    sair = input('DESEJA SAIR ?  [s] PARA SIM | [n] PARA NÃO: ')
SystemExit('s')