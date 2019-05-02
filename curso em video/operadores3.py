print('AULA 08 MEDIDAS ')
medida = float(input('DIGITE AQUI NUMEROS PARA SEREM TRANSFORMADOS EM DISTANCIA:  '))
cm = medida * 100
mm = medida * 1000
km = medida *1
dam = medida *10000
print(' A MEDIDA DE {}cm CORRESPONDE A  {:.0f}cm !\n E EM mm CORRESPONDE A  {:.0f}mm !\n e km é {:.0f}! dam {}!'.format(medida,cm,mm,km,dam,end=' '))