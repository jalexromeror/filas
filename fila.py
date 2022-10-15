import os
import random as rd

# Función para borrar pantalla.
def borrar_pantalla():
    comando = 'clear'
    if os.name in ('nt', 'dos'):
        comando = 'cls'
    os.system(comando)

# Programa principal.
def run():  
    borrar_pantalla()    
    DIAS = 5
    MINUTOS = 480
    espera = []    
    for dia in range(DIAS):
        k = 0
        caja = []
        espera.append(rd.randint(7, 12))
        # espera.append(3)
        for minuto in range(MINUTOS):
            caja.append(rd.randint(10, 15))
            # caja.append(5)
            print('dia = ' + str(dia), end='')
            print('\t min = ' + str(minuto), end='')
            while minuto == (espera[len(espera)-1] + k*caja[len(caja)-1]):
                print('\t k = ' + str(k), end='')
                k += 1                    
            print('')

# Ejecición del programa.
if __name__ == '__main__':    
    run()
