import math #COM BIBLIOTECA MATH

co = float(input('digite: '))
ca = float(input('novamente: '))
hi = math.hypot( co , ca )#(co **2 + ca **2) ** (1/2) SEM A BIBLIOTECA MATH
print(' A hipotenusa de {} x {} é igual = {:.2f}'.format(co , ca , hi))
