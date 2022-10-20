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

def diccionario_a_lista(dic):
    items = dic.items()
    frecuencia = []
    for item in items:
        lista = [item[0], item[1]]
        frecuencia.append(lista)
    return frecuencia

def acumula_frecuencia(letra, dic):
    if letra in dic:
        dic[letra] = dic[letra] + 1
    else:
        dic[letra] = 1
    return dic

def lectura(nombre):
    ent = open(nombre + '.txt')
    dic = {}
    for linea in ent:
        for letra in linea:
            dic = acumula_frecuencia(letra, dic)
    ent.close()
    frecuencia = diccionario_a_lista(dic)
    return frecuencia

def agrega_ceros(elem):
    while len(elem) < 4:
        elem = '0' + elem
    return elem

def prepara(frecuencia):
    lista = []
    for elemento in frecuencia:
        elem = agrega_ceros(str(elemento[1]))  
        lis = str(elem + elemento[0])
        lista.append(lis)
    lista.sort(reverse = True)
    return lista

def ordena(frecuencia):
    lista_ordenada = prepara(frecuencia)
    lista = []
    for elem in lista_ordenada:
        frecu = int(elem[0:4])
        letra = elem[4:]
        lista.append([letra, frecu])
    return lista

def genera_salida(nombre, frecuencia_final):
    sal = open(nombre + '_frec.txt', 'w')
    for elem in frecuencia_final:
        linea = elem[0] + ' ' + str(elem[1]) + '\n'
        sal.write(linea)
    sal.close()

if __name__ == '__main__':
    limpia_pantalla()
    nombre = input('Nombre del archivo: ')
    frecuencia_inicial = lectura(nombre)
    frecuencia_final = ordena(frecuencia_inicial)
    muestra_pantalla(frecuencia_final)
    genera_salida(nombre, frecuencia_final)
