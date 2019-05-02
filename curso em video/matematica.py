a = int(input('Digite o Valor de A: '))
b = int(input('Digite o  Valor de B: '))
raiz = 0

if a == 0:
    print ('Nao e funcao do primeiro grau')
if a > 0:
    print ('Essa funcao e do primeiro grau e crescente')
if a < 0: 
    print ('Essa funcao e do primeiro grau e decrescente')

raiz = -(b/a)
print ('O valor da raiz é:{},  O intercepto em y é:{}'.format(raiz,b))