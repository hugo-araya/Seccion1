def fib_iter(numero):
    primero = 0
    segundo = 1
    suma = 0
    cont = 1
    while(cont <= numero):    
        cont = cont + 1
        primero = segundo
        segundo = suma
        suma = primero + segundo	
    return(suma)

if __name__ == '__main__':
    n=int(input("Valor para 'n': "))
    i = 2
    lista = [0, 1]
    while i <= n:
        lista = lista + [fib_iter(i)]
        i = i + 1
    print(lista)
    pares = []
    for elem in lista:
        if elem % 2 == 0:
            if elem != 0:
                pares = pares +[elem]
    print(pares)
