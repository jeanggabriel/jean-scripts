import csv
a = input('Nome : ')
b = input('Endereço : ')
c = input('Cidade : ')
d = input('Estado : ')
e = input('CEP : ')
geral = str(a)+'\n'+(b)+'\n'+(c)+'\n'+(d)+'\n'+(e)+'\n'
arquivo = open("informaçoes.csv", "w")
arquivo.write(geral)
arquivo.close()

import csv
arquivo = open("informaçoes.csv", "w")
a = input('Nome : ')
b = input('Endereço : ')
c = input('Cidade : ')
d = input('Estado : ')
e = input('CEP : ')
cabecalho = 'Nome;Endereço;Cidade;Estado;CEP\n'

geral = str(a)+';'+(b)+';'+(c)+';'+(d)+';'+(e)+';'

arquivo.write(cabecalho)
arquivo.write(geral)
arquivo.close()

print('INFORMAÇOES SALVAS  ;)  ')

