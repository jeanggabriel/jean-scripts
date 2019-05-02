from bs4 import BeautifulSoup
import requests 
import pymongo
from lxml import html
import time
import random
import re
import os
import logging
import datetime
from http.cookiejar import LWPCookieJar
import facebook

listanomes = [' /tinapompeia ' , ' /tina.januarioii.3 ']

for j in listanomes:
	req = requests.get ('https://www.facebook.com/tinapompeia'+str(j))
	requisiçao = requests.get ('https://www.facebook.com/tina.januarioii.3\n'+str(j))
	soup0 = BeautifulSoup(requisiçao.content,'html.parser')
	soup = BeautifulSoup(req.content,'html.parser')

	mapeamento = soup0.select('div div div')
	buscar = soup0.find_all('div',{'class':"mainContainer"})
	mapeamento2 = soup.select('div div div div')

if mapeamento2 == listanomes:
    	l.append(mapeamento2)
#mapeamento2 = soup.find_all('span',{'class':'_2iem'})
def criaSession(login, senha): #Função para armazenamento de Cookies Locais
		s.cookies = LWPCookieJar('cookiejar')
		if not os.path.exists('cookiejar'):
			print('.:: Armazenando Cookies ::.')
			s.cookies.save()
			loginFacebook(login, senha)
		else:
			print('.:: Carregando Cookies ::.')
			s.cookies.load(ignore_discard=True)
			req = s.get('https://m.facebook.com/')
			soup = BeautifulSoup(req.content,'html.parser')
			
			textoSoup = str(soup)
			if textoSoup.find("Participe do Facebook") != 0:
				loginFacebook(login, senha)
		s.cookies.save(ignore_discard=True)

def loginFacebook(email,senha): #Função para Login no Facebook
	vetor1 = []
	vetor2 = []

	req = requests.get('https://m.facebook.com/')
	soup = BeautifulSoup(req.content,'html.parser')

	for x in soup.find_all('input'):
		requisicao = x['name']
		if str(requisicao) == 'lsd' or str(requisicao) == 'li' or str(requisicao) == 'm_ts':
			vetor1.append(requisicao)
			resposta = x['value']
			vetor2.append(resposta)
			
	dicionario = dict(zip(vetor1,vetor2))

	dicionario['email'] = email
	dicionario['pass'] = senha
	dicionario['login'] = 'Log In'

	r = s.post('https://m.facebook.com/login.php?refsrc=https%3A%2F%2Fm.facebook.com%2F&amp;refid=8', data=dicionario)
	timeRandom = random.randint(10, 25)
	time.sleep(timeRandom)


for i in mapeamento2:
    print(i.text)
for x in mapeamento:
	print (x.text)