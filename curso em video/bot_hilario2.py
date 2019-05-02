from bs4 import BeautifulSoup
import requests

site = requests.get('https://dolarhoje.com/')
soup = BeautifulSoup(site.content,'html.parser')
soup0 = soup0.select('input#nacional')
soup1 = soup1.find_all('span',{'class':'cotMoeda nacional'})
soup2 = soup2.find_all('input')
soup3 = soup3.select('input[ id |=estrangeiro]')
soup4 = soup4.select('input[ id |=nacional]')
for i in soup3 and soup4:
    print(i)
