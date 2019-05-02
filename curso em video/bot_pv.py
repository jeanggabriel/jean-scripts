from bs4 import BeautifulSoup
import requests

site = requests.get('http://pv.org.br/parlamentares/nos-legislativos-municipais/')
soup = BeautifulSoup(site.content,('html.parser'))
soup1 = soup.select('div#search-form')
soup2 = soup.find_all('div',{'class':'wpb_wrapper1'})
soup3 = soup.find_all('strong')
soup4 = soup.find_all('td')
soup5 = soup.find_all('tr')
soup6 = soup.find_all('td')
soup7 = soup.find_all('tr')
soup8 = soup.find_all('tbody')

for i in (soup1):
    for x in (soup2):
        for l in (soup3):
            for h in (soup4):
                print ([i.text.replace('\n',''),[x.text],[l.text],[h.text]])
