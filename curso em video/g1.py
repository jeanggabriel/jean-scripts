from bs4 import BeautifulSoup
import requests
import html5lib

site = requests.get('https://g1.globo.com/busca/?q=agrotoxico')
soup = BeautifulSoup(site.content ,'html.parser')
link = soup.select('div.widget--info__text-container a')
for x in link:
    link2 = x['href']
    site2 = requests.get('https:'+str(link2))
    soup2 = BeautifulSoup(site2.content,'html.parser')
    seguranca = str(soup2).split('"')
    seguranca2 = seguranca[5]
    site3 = requests.get(seguranca2)
    soup3 = BeautifulSoup(site3.content,'html.parser')
    titulo =soup3.find_all('h1',{'class':'content-head__title'})
    noticia = soup3.find_all('p',{'class':'content-text__container theme-color-primary-first-letter'})
    noticia2 = soup3.find_all('p',{'class':'content-text__container'})
    for a in titulo:
        print(10*'-')
        print('                           .::TITULO DA NOTICIA::.                                        ')
        print(a.text)
        for b in noticia:
            print('                           .::NOTICIA::.                                        ')
            print(b.text)
            for c in noticia2:
                print(c.text)
                
    