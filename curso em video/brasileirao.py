from bs4 import BeautifulSoup
from lxml import html
import requests

hr = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
	'cache-control': 'max-age=0',
	'cookie': '__cfduid=d863d4d01c6e23ab5288a084db923d7cb1541440572; _ga=GA1.2.692560380.1541440574; _gid=GA1.2.910022917.1541440574; _gat_UA-820510-2=1; _gat=1; _fbp=fb.1.1541440577206.2107183919; __gads=ID=b41ee561ac174450:T=1541440577:S=ALNI_Mb_GrRPmCuY1YBO5gf_H9NdvnhqiQ',
	'referer': 'https://www.google.com.br/',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}

requisiçao = requests.get('https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-a/',headers=hr)
soup = BeautifulSoup(requisiçao.content,'html.parser')
nomeTime = soup.select('tbody td.table__team a')
for key ,i in enumerate(nomeTime):
	nomeTime = i.text
	print(str(nomeTime.replace(';','')))
