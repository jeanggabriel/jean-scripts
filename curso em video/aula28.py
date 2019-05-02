from random import randint
while True:
    print('-=-'* 10)
    print('Digite um numero entre 0 e 5 e tente adivinhar... ')
    print('-=-'* 10)
    computador = randint(0,5)
    usuario = int(input('digite um numero para ser adivinhado '))
if usuario == computador:
    print('você Ganhou com o numero {} o computador perdeu com o numero {}'.format(usuario,computador))
else:
    print('o computador ganhou com o numero {} e o numero que vc escolheu foi {}'.format(computador,usuario))
    a = input('deseja jogar novemente ? s ou n   ')
if a == 's':
    pass
else:
    SystemExit()
for x in range(0,100):
    print(x)

