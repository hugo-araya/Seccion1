# Hugo Araya Carrasco
# Seccion: Todas
# Fecha: 18 de Octubre 2022

import os

def limpia_pantalla():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def muestra_pantalla(frecuencia):
    print('Analisis Frecuencia de Caracteres')
    print('---------------------------------')
    for elem in frecuencia:
        print(elem[0], elem[1])

if __name__ == '__main__':
    limpia_pantalla()
    nombre = input('Nombre del archivo: ')
    frecuencia_inicial = lectura(nombre)
    frecuencia_final = ordena(frecuencia_inicial)
    muestra_pantalla(frecuencia_final)
    genera_salida(nombre, frecuencia_final)
