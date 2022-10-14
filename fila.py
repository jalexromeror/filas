import os
import random as rd

def borrar_pantalla():
    comando = 'clear'
    if os.name in ('nt', 'dos'):
        comando = 'cls'
    os.system(comando)

def run():  
    borrar_pantalla()    
    DIAS = 1
    MINUTOS = 20
    espera = []    
    for dia in range(DIAS):
        k = 0
        caja = []
        atencion = []
        # espera.append(rd.randint(2, 3))
        espera.append(3)
        for minuto in range(MINUTOS):
            # caja.append(rd.randint(4, 5))
            caja.append(5)
            print('dia = ' + str(dia), end='')
            print('\t min = ' + str(minuto), end='')
            while minuto == (espera[len(espera)-1] + k*caja[len(caja)-1]):
                print('\t k = ' + str(k), end='')
                k += 1                    
            print('')

if __name__ == '__main__':    
    run()
