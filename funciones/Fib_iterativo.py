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
    print("Fibonacci:", fib_iter(n))


