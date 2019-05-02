from bs4 import BeautifulSoup
from lxml import html
import requests
import random
import time

timeRandom = random.randint(8, 20)
time.sleep(timeRandom)
req = requests.get('https://megafilmes.org/?s=disney')
soup = BeautifulSoup(req.content,'html.parser')
b = soup.find_all('div',{'class':'row listagem'})
a = soup.select('div')
for i in b:
        print(i.text)
for x in a:
        print(x.text)