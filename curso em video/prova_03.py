def soma(x,y):
    return x + y

def subtraçao(x,y):
    return x - y

def multiplicaçao(x,y):
    return x * y

def divisao(x, y):
    return x / y

print('selecione uma operaçao: ')
print('1. soma')
print('2. subtraçao')
print('3. multiplicaçao')
print('4. divisao ')

escolha = str(input('entre com a escolha:  >>> 1/2/3/4 <<<'))
num1 = int(input('Entre com o primeiro numero: '))
num2 = int(input('Entre com o segundo numero: '))

if escolha =='1':
    print('soma: {0} + {1} = {2}'.format(num1,num2,soma(num1,num2)))
elif escolha =='2':
    print('subtraçao: {0} - {1} = {2}'.format(num1,num2,subtraçao(num1,num2)))
elif escolha =='3':
    print('multiplicaçao {0} * {1} = {2}'.format(num1,num2,multiplicaçao(num1,num2)))
elif escolha =='4':
    print('divisao {0} / {1} = {2} '.format(num1,num2,divisao(num1,num2)))
else:
    print('entrada invalida')