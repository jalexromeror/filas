import random as rd

def run():
    espera = rd.randint(2, 3)
    caja = rd.randint(4, 5)
    minutos = 25
    k = 0
    for minuto in range(minutos):
        print('minuto = ' + str(minuto), end='')            
        while minuto == (espera + k * caja):
            espera = rd.randint(2, 3)
            caja = rd.randint(4, 5)
            print('\tespera = ' + str(espera), end='')
            print('\tcaja = ' + str(caja))
            k += 1
        print('')
        
if __name__ == '__main__':
    run()

