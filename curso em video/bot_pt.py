from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.haddadpresidente.com.br/doe/')
soup = BeautifulSoup(site.content,('html.parser'))
soup1 = soup.select('div_ngcontent-c0')
soup2 = soup.select('div_ngcontent-c4')
soup3 = soup.select('b_ngcontent-c4')
soup4 = soup.find_all('div')

for i in soup4:
    print(i.text)