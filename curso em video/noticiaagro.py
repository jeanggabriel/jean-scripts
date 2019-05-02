#noticias agricolas 
from bs4 import BeautifulSoup
import requests
#import csv
requests = requests.get('https://www.noticiasagricolas.com.br/clima/')
soup = BeautifulSoup(requests.content,'html.parser')
selecionar = soup.select('aside sidebar')
buscas = soup.findAll('div',{'class':'wrapper container content-container'})
buscar1 = soup.findAll('div',{'class':'box'})
buscar2 = soup.findAll('div',{'class':'wrap-cot-table'})
buscar3 = soup.findAll('td',{'class':'first'})
buscar4 = soup.findAll('div',{'class':'cotacao cotacao-investing loaded'})
selecionar1 = soup.select('table cross_rate_1')
buscar5 = soup.findAll('tbody')
#print(buscas)
for i in buscar2:
    print(i.text)
    for j in buscar3:
        print(j.text)
        for k in buscar5:
            print(k.text)






