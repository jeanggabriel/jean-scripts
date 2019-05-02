import requests
from lxml import html
import pymongo


conexao = pymongo.MongoClient("mongodb+srv://mongofretefacil:<password>@cluster0-ehviq.mongodb.net/test?retryWrites=true")
Mydb = conexao['fretefacil']

print('Aula Bot Hilario')
listamoedas = ['/', '/bitcoin-hoje', '/ethereum/', '/litecoin/']
for i in listamoedas:

    requisicao = requests.get('https://dolarhoje.com'+str(i))

    tree = html.fromstring(requisicao.content)

    real = tree.xpath('//*[@id="estrangeiro"]')[0].value
    moeda = tree.xpath('//*[@id="nacional"]')[0].value
    print('='*20)
    print('Real :R$ {}\nEstrangeiro :US$ {:.5} \n'.format(real,moeda))
