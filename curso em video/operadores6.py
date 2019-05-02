print('AULA 11 LARGURA DE UMA PAREDE ')
larg = float(input('QUAL A LARGURA DA PAREDE: '))
alt = float(input('QUAL A ALTURA DA SUA PAREDE: '))
area = larg * alt
print('SUA LARGURA É DE {} X {} E SUA AREA É DE {} m²'.format(larg,alt,area))
tinta = area / 2
print('PARA PINTAR ESSA PAREDE PRECISARA DE {:.3f} LITROS DE TINTA'.format(tinta))
