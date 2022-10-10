import random as rd

def run():
    dias = 1
    minutos = 15
    for dia in range(dias):
        print('dia = ' + str(dia), end='')        
        for minuto in range(minutos):
            espera = rd.randint(2, 3)
            caja = rd.randint(4, 5)
            print('\tminuto = ' + str(minuto), end='')    
            if (minuto >= 0) & (minuto <= espera):                
                print('\tespera = ' + str(espera), end='')
                print('')            
            elif minuto > espera:
                print('',end='')
                print('\tcaja = ' + str(caja))


if __name__ == '__main__':
    run()