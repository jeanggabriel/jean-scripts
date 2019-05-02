from bs4 import BeautifulSoup
import requests
from lxml import html

nome = input('digite um comentario')
requisiçao = requests.get('https://www.facebook.com/')
soup = BeautifulSoup(requisiçao.content,'html.parser')
a = soup.find_all('div',{'class':  '_3d2q _65tb _7c_r _4w79'+str(nome)})
for i in a:
    print(i)

