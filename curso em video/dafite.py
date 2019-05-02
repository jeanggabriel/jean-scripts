import requests
from bs4 import BeautifulSoup
from lxml import html
import wget

#url = 'https://dafitistatic-a.akamaihd.net/p/Colcci-Bon%C3%A9-Colcci-Trucker-Logo-Bege/Preto-0152-8986683-1-zoom.jpg'
#escolher = int(input('digite [ 1 ] para bones [ 2 ] para ver os preços: '))
requisiçao = requests.get('https://www.dafiti.com.br/bolsas-e-acessorios-masculinos/bones-e-chapeus/')
soup = BeautifulSoup(requisiçao.content,'html.parser')
bones = soup.find_all ('div',{'class':'product-box-brand'})
preço = soup.find_all ('div',{'class':'product-box-price is-special-price'})
#filename = wget.download(url)

for i in bones:
        for x in preço:
                print ('BONES:{} PREÇOS:{}'.format([i.text.replace("[","")],[x.text.replace('\n','')]))                        