import csv
arquivo = open("eleiçoes.csv", "w")

contadorBolsonaro = 0
contadorHaddad = 0
contadordoria = 0
contadormarciofrança = 0
contadorBranco = 0
contadorNulo = 0

while True:
	print('\n====> CANDIDATOS <====\n')
	print('\n==== JAIR BOLSONARO 17 PSL ====')
	print('\n==== FERNANDO HADDAD 13 PT ====')
	print('\n==== JOÃO DORIA 45 PSDB ====')
	print('\n==== MARCIO FRANÇA 40 PSB ====')
	print('\n======================================\n')
	print('==== VOTOS NULO | VOTOS BRANCO ====\n')
	print('==== NULO 0  ====')
	print('\n==== BRANCO 1 ====')
	
	quantidadeVotos = int(input("\n\nInsira os VOTOS: "))
	candidatoVotos = int(input("\nInsira o numero do canditado:\n| 13 HADDAD PT|\n|17 BOLSONARO PSL|\n|45 DORIA|\n|40 MARCIO FRANÇA|\n|1 BRANCO|\n|0 NULO |\n:  "))

	
	if candidatoVotos == 17:
		contadorBolsonaro += quantidadeVotos
	elif candidatoVotos == 13:
		contadorHaddad += quantidadeVotos
	elif candidatoVotos == 45:
		contadordoria +=quantidadeVotos
	elif candidatoVotos == 40:
		contadormarciofrança += quantidadeVotos
	elif candidatoVotos == 1: 
		contadorBranco += quantidadeVotos
	elif candidatoVotos == 0:
		contadorNulo += quantidadeVotos
		
	
	confirmacao = input("Deseja Inserir Novamente ? [s] PARA [SIM]  ou [n] PARA [NÃO] :  ")
	
	if str(confirmacao) == "n":
		break
	elif str(confirmacao) == "s":
		pass
	else:
		pass
		
print ("\n=========== RESULTADO DA VOTAÇÃO PARA PRESIDENCIA! ========== \n")
while contadorBolsonaro > contadorHaddad:
	print('BOLSONARO GANHOU com {} VOTOS'.format(contadorBolsonaro))
	break
	print ("Votos Para BOLSONARO PSL: "+str(contadorBolsonaro))
	print('\n')
while contadorHaddad > contadorBolsonaro:
	print('HADDAD GANHOU com {} VOTOS'.format(contadorHaddad))
	break	
	print ("Votos Para HADDAD PT:  "+str(contadorHaddad))
	print('\n')
print("\n=========== RESULTADO DA VOTAÇÃO PARA GOVERNADOR! ========== \n")
while contadordoria > contadormarciofrança:
	print('DORIA GANHOU COM {} VOTOS'.format(contadordoria,end=('\n')))
	break
	print('Votos Para JOÃO DORIA PSDB: '+str(contadordoria))
	print('\n')
while contadormarciofrança > contadordoria:
	print('MARCIO FRANÇA GANHOU COM {} VOTOS'.format(contadormarciofrança,end=('\n')))
	break
	print('votos Para MARCIO FRANÇA PSB: '+str(contadormarciofrança))
	print('\n')

print ("\n=========== RESULTADO DA VOTAÇÃO PARA PRESIDENCIA! ========== \n")
print('BOLSONARO {} VOTOS'.format(contadorBolsonaro))
print('HADDAD {} VOTOS'.format(contadorHaddad))
print('\n')
print("\n=========== RESULTADO DA VOTAÇÃO PARA GOVERNADOR! ========== \n")
print('JOÃO DORIA {} VOTOS'.format(contadordoria))
print('MARCIO FRANÇA {} VOTOS'.format(contadormarciofrança))
print('\n')
print('=========== RESULTADO DE NULOS E BRANCOS! ==========')
print ("Votos BRANCO: "+str(contadorBranco))
print ("Votos NULO: "+str(contadorNulo))
print('\n')

bozonaro  = 'Bolsonaro ; ' + str(contadorBolsonaro) + '\n'
hadadis = 'Haddad ; '+ str(contadorHaddad) + '\n'
dorinha = 'João doria ;'+ str(contadordoria) + '\n'
frança = 'Marcio frança ;' + str(contadormarciofrança) + '\n'
branco = 'Branco ;' + str(contadorBranco) + '\n'
nulo = 'Nulo ;' + str(contadorNulo) + '\n'
cabecalho2 = 'Candidato ; Votos \n'
arquivo.write(cabecalho2)
arquivo.write(bozonaro)
arquivo.write(hadadis)
arquivo.write(dorinha)
arquivo.write(frança)
arquivo.write(branco)
arquivo.write(nulo)
arquivo.close()