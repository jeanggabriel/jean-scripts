menor = int(input('entre com a menor busca da faixa de busca'))
maior = int(input('entre com o maior numero da faixa de busca'))
print ('os numeros primos entre {0} e {1} são :'.format(menor,maior))
for num in range(menor,maior + 1):
    if num >1:
        for i in range(2,num):
            if (num % i ) == 0:
                break
        else:
            print(num)
            print('certo!')