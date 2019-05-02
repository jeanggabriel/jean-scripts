print ("\n Programa em Python para resolver um sistema de equa��es com tr�s inc�gnitas")
print ("\n Estou definindo um sistema de tr�s equa��es com tr�s inc�gnitas desta forma:")
print ("\n \n ax + by + cz = R1 \n dx + ey + fz = R2 \n gx + hy + iz = R3 \n")
print ("\n Digite os valores para: \n")

# O usu�rio d� valores aos coeficientes

a = int(input("a  \n"))
b = int(input("b  \n"))
c = int(input("c  \n"))
r1 = int(input("r1  \n"))
d = int(input("d  \n"))
e = int(input("e  \n"))
f = int(input("f  \n"))
r2 = int(input("r2  \n"))
g = int(input("g  \n"))
h = int(input("h  \n"))
i = int(input("i  \n"))
r3 = int(input("r3  \n"))

# Aqui � a regra de Cramer, propriamente dita.

det = ((a * e * i) + (b * f * g) + (c * d * h)) - ((c * e * g) + (a * f * h) + (b * d * i))
detx = ((r1 * e * i) + (b * f * r3) + (c * r2 * h)) - ((c * e * r3) + (r1 * f * h) + (b * r2 * i))
dety = ((a * r2 * i) + (r1 * f * g) + (c * d * r3)) - ((c * r2 * g) + (a * f * r3) + (r1 * d * i))
detz = ((a * e * r3) + (b * r2 * g) + (r1 * d * h)) - ((r1 * e * g) + (a * r2 * h) + (b * d * r3))

# Define os valores das inc�gnitas, com casas decimais.
if ((det == 0) and (detx !=0) and (dety !=0) and (detz !=0)):
   print ("\n\n ====[ Sistema Imposs�vel ]====")
elif ((det == 0) and (detx == 0) and (dety == 0) and (detz == 0)):
   print("\n\n ====[ Sistema Poss�vel e Indeterminado ]====" ) 
else:
   x = (round(detx, 3) / round(det, 3))
   y = (round(dety, 3) / round(det, 3))
   z = (round(detz, 3) / round(det, 3)) 
   print ("\n\n====[ Sistema Possivel e Determinado ]====")
   print ("\nOs resultados s�o (aproximados com 4 casas decimais):")
   print ("\n x = %.4f" % x)
   print ("\n y = %.4f" % y)
   print ("\n z = %.4f" % z)
print()

# Fim
