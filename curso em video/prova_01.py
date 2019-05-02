import math
tmatriz = int (input('digite o tamanho da matriz ? '))
if (tmatriz == 0) or (tmatriz < 0):
    print ('Tamanho Invalido!')
    quit()
matriz = [0]*tmatriz
for i in range(tmatriz):
    matriz[i] = [0]*tmatriz
for i in range(tmatriz):
    for j in range(tmatriz):
        matriz[i] [j] = i+j
aux = tmatriz-1
total = 0
for i in range(tmatriz):
    total = total + matriz[i] [aux]
    aux = aux -1
for i in range(tmatriz):
    print (matriz[i] [:])
print ('Média: ', total/int(tmatriz))


