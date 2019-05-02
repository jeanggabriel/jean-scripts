n1 = int(input('Digite um Numero '))
n2 = int(input('Digite outro Numero '))

if n1 > n2:
    maior = n1
else:
    maior = n2
while True:
    if maior % n1 == 0 and maior % n2 == 0:
        print(maior)
        break
    else:
        maior += 1