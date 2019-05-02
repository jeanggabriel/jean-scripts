import random

n1 = str(input('DIGITE O NOME DO PRIMEIRO ALUNO: '))
n2 = str(input('NOME DO SEGUNDO ALUNO: '))
n3 = str(input('NOME DO TERCEIRO ALUNO: '))
n4 = str(input('NOME DO QUARTO ALUNO: '))

lista = [ n1 ,n2 ,n3 ,n4 ]
#escolhido = random.shuffle(lista)#tambem tem o ramdom >>> choice  == escolha
random.shuffle(lista)
print('O ALUNO ESCOLHIDO FOI >>>=  {}  =<<<'.format(lista))#ou escolhido
#for i in random(n1,n2,n3,n4):
 #   print(i)