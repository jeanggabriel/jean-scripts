print('AULA 12 CALCULANDO DESCONTOS')
desconto = float(input('DIGITE UM VALOR PARA SER DESCONTADO R$ '))
n = desconto - (desconto * 5 / 100)
print('O PRODUTO CUSTAVA {:.2f}! \n PROMOÇÃO COM 5% DE DESCONTO IRÁ CUSTAR R$ {:.2f} !\n'.format(desconto,n))