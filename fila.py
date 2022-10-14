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
    espera = []    
    for dia in range(DIAS):
        k = 1
        caja = []
        atencion = []
        espera.append(rd.randint(2, 3))        
        for minuto in range(MINUTOS):
            caja.append(rd.randint(4, 5))
            print('dia = ' + str(dia), end='')
            print('\t min = ' + str(minuto), end='')
            if not (minuto >= 0) & (minuto <= espera[len(espera)-1]):
                print('\t dif = ' + str(minuto-espera[len(espera)-1]-1), end='')
                if (minuto-espera[len(espera)-1]-1) == (k*caja[len(caja)-1]-1):
                    atencion.append(caja[len(caja)-1])
                    print('\t k = ' + str(k), end='')
                    k += 1                    
            print('')

if __name__ == '__main__':    
    run()