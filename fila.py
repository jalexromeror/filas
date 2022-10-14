import os
import random as rd

def borrar_pantalla():
    comando = 'clear'
    if os.name in ('nt', 'dos'):
        comando = 'cls'
    os.system(comando)

def run():
    borrar_pantalla()    
    DIAS = 2
    MINUTOS = 30
    # esperar = [7,8,9,10,11,12]
    # atender = [10,11,12,13,14,15]
    # esperar = [2,3]
    # atender = [4,5]
    # k = 0
    espera = []    
    for dia in range(DIAS):
        k = 1
        caja = []
        atencion = []
        # momento = rd.choice(esperar)
        # espera.append(momento)
        # espera.append(rd.choice([7,8,9,10,11,12]))
        # espera.append(rd.choice(list(range(7, 13))))
        # espera.append(rd.randint(2, 3))
        espera.append(3)
        for minuto in range(MINUTOS):
            # devuelta = rd.choice(atender)
            # caja.append(devuelta)
            # caja.append(rd.choice([10,11,12,13,14,15]))
            # caja.append(rd.choice(list(range(10, 16))))
            # caja.append(rd.randint(4, 5))
            caja.append(5)
            print('dia = ' + str(dia), end='')
            print('\t min = ' + str(minuto), end='')
            # print('\t L_es = ' + str(espera), end='')
            print('\tesp = ' + str(espera[len(espera)-1]), end='')
            print('\tcaja = ' + str(caja[len(caja)-1]), end='')
            # print('\t L_ca = ' + str(caja), end='')
            if not (minuto >= 0) & (minuto <= espera[len(espera)-1]):
                print('\t ESP', end='')
                print('\t dif = ' + str(minuto-espera[len(espera)-1]-
                1), end='')
                if (minuto-espera[len(espera)-1]-1) == (k*caja[len(caja)-1]-1):
                    # print('\t OK', end='')
                    atencion.append(caja[len(caja)-1])
                    print('\t k = ' + str(k), end='')
                    # print('\t' + str(atencion), end='')
                    k += 1                    
            else:
                print('\t N_ESP', end='')
            print('')
    print(espera)
    print(atencion)

if __name__ == '__main__':    
    run()