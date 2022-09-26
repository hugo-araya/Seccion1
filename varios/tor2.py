import turtle

def triangulo():
    for i in range(3):
        flecha.forward(100) 
        flecha.left(120)

def cuadrado():
    for i in range(4):
        flecha.forward(100) 
        flecha.left(90)

def pentagono():
    for i in range(5):
        flecha.forward(100) 
        flecha.left(72)

if __name__ == "__main__": 
    ventana = turtle.Screen() 
    flecha = turtle.Turtle() 
    for i in range (12):
        # triangulo()
        # cuadrado()
        pentagono()
        flecha.right(30)
        flecha.forward(20)

    ventana.mainloop()