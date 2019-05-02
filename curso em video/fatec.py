from bs4 import BeautifulSoup
import requests
import csv
from lxml import html
import html5lib


jurozin = open ('Juros.csv', 'w')

requests = requests.get('https://www.konkero.com.br/financiamento/carro/melhores-taxas-de-financiamento-de-carro-brasil')
soup = BeautifulSoup(requests.content,'html.parser')

posicao = soup.select('table[width|=415] tr td[width|=76]')
instituicao = soup.select('table[width|=415] tr td[width|=127]')
jurosmes = soup.select('table[width|=415] tr td[width|=117]')
jurosano = soup.select('table[width|=415] tr td[width|=95]')
soup2 = soup.select('table[width|=427] tr td[width|=114]')



cabecalho = 'Posição ; Instituição ; Juros/Mes ; Juros/Ano \n'
jurozin.write(cabecalho)

for i in range(len(posicao)):
    print (posicao[i].text, instituicao[i].text, jurosmes[i].text, jurosano[i].text)
    aux = posicao[i].text + ' ; '+ instituicao[i].text + ' ; ' + jurosmes[i].text + ' ; ' + jurosano[i].text + '\n'
    jurozin.write(aux)