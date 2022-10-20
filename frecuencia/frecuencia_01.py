# Hugo Araya Carrasco
# Seccion: Todas
# Fecha: 18 de Octubre 2022

if __name__ == '__main__':
    nombre = input('Nombre del archivo: ')
    frecuencia_inicial = lectura(nombre)
    frecuencia_final = ordena(frecuencia_inicial)
    muestra_pantalla(frecuencia_final)
    genera_salida(nombre, frecuencia_final)
