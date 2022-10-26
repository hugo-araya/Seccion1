def Fibonacci(numero):
    if(numero==0):
        return 0
    elif(numero==1):
        return 1
    else:
        return (Fibonacci(numero-2)+Fibonacci(numero-1))

if __name__ == '__main__':
    n=int(input("Valor para 'n': "))
    print("Fibonacci:", Fibonacci(n))

