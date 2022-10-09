import random as rd

def run():

    # espera = rd.randint(2, 3)
    # caja = rd.randint(4, 5)
    minutos = 15
    for minuto in range(minutos):
        espera = rd.randint(2, 3)
        caja = rd.randint(4, 5)
        print('minuto = ' + str(minuto), end='')    
        if (minuto >= 0) & (minuto <= espera):
            print('\tespera = ' + str(espera), end='')
            print('\tcaja = N/A')
        else:
            print('\tespera = N/A', end='')
            print('\tcaja = ' + str(caja))

if __name__ == '__main__':
    run()