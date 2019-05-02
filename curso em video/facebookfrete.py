from bs4 import BeautifulSoup
from lxml import html
import html5lib
import requests
import json
import time
import random

timeRandom = random.randint(8, 20)
time.sleep(timeRandom)

req = requests.get('https://www.facebook.com/')
soup = BeautifulSoup(req.content,'html.parser')
soup1 = soup.find_all('span',{'class':'hasCaption'},'span')
for i in soup1:
    print(i.text)