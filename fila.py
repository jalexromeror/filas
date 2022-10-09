import random as rd

minutos = 15
espera = rd.randint(2, 3)
caja = rd.randint(4, 5)
k = 0
for minuto in range(minutos):
    espera = rd.randint(2, 3)
    caja = rd.randint(4, 5)    
    print('minuto = ' + str(minuto), end='')
    print('\tk = ' + str(k), end='')
    print('\tespera = ' + str(espera), end='')
    print('\tcaja = ' + str(caja))
    k += 1