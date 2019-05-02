from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.nexojornal.com.br/interativo/2016/01/11/O-seu-sal%C3%A1rio-diante-da-realidade-brasileira')
soup = BeautifulSoup(req.content,'html.parser')
soup1 = soup.select('span#id=valor-uf-numero')
print('AULA 13 REAJUSTE SALARIAL')
while True:
    salario = float(input('DIGITE SEU SALARIO ?  R$: '))
    aumento = float(input('QUANTOS % DE AUMENTO VOCÊ RECEBEU ? R$:'))
    aut = salario + (aumento * salario /100) 
    #reajuste = salario + (salario *15 / 100)
    print('O SEU SALARIO DE R$ {:.2f}, COM REAJUSTE SALARIAL FOI PARA R$ {:.2f}'.format(salario,aut))
    a = str(input('Deseja continuar ?   S [SIM]  N [NÃO] '))
    if str(a) == 'n':
        print('== == == ATENÇÃO ! == == ==',end=' \n ')
        print('seu salario foi reajustado para {:.2f}'.format(aut))
        break
    elif str(a) == 's':
        pass
    else:
        pass
    print('== == == ATENÇÃO ! == == ==',end=' \n ')
    print('='*50)
    print('Salario Foi Reajustado para {:.2f}'.format(aut))
for i in soup:
    print(i.text)