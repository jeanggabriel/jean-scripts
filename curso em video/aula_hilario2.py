def calculando_dobro(num):
    dobro = num*2
    return(dobro)

num = int(input('Digite um Numero '))
resultado = calculando_dobro(num)
print('Dobro de {} é {}'.format(num,resultado))