import requests
import html5lib
from bs4 import BeautifulSoup
from lxml import html

req = requests.get('https://globoesporte.globo.com/futebol/libertadores/')
soup = BeautifulSoup(req.content,'html.parser')
a = soup.find_all('h2',{'class':'classificacao__header--titulo'})
b = soup.find_all('th',{'class':'tabela__head--coluna tabela__head--classificacao'})
print(soup)