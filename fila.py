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
    MINUTOS = 15
    # k = 0
    espera = []    
    for dia in range(DIAS):
        caja = []
        # espera.append(rd.randint(3, 4))
        espera.append(3)
        for minuto in range(MINUTOS):
            # caja.append(rd.randint(5, 6))
            caja.append(5)
            print('dia = ' + str(dia), end='')
            print('\t min = ' + str(minuto), end='')
            # print('\t L_es = ' + str(espera), end='')
            print('\t esp = ' + str(espera[len(espera)-1]), end='')
            print('\t caja = ' + str(caja[len(caja)-1]), end='')
            # print('\t L_ca = ' + str(caja), end='')
            if not (minuto >= 0) & (minuto <= espera[len(espera)-1]):
                print('\t ESP', end='')
                print('\t dif = ' + str(minuto-espera[len(espera)-1]-
                1), end='')
            else:
                print('\t N_ESP', end='')
            print('')

if __name__ == '__main__':    
    run()