from turtle import *
def estrellas_personalizada():
    numero_de_picos = int(input("Introduzca el numero de picos: "))
    if numero_de_picos <= 4:
        angulo = 360 / numero_de_picos
    elif numero_de_picos == 36:    
        angulo = 170
    elif numero_de_picos == 72:
        angulo = 175
    elif numero_de_picos == 24:
        angulo = 165
    elif numero_de_picos == 12:
        angulo = 150
    elif numero_de_picos == 6:
        angulo = 120
    elif numero_de_picos == 9:
        angulo = 160
    elif numero_de_picos == 18:
        angulo = 140
    elif numero_de_picos == 27:
        angulo = 130
    else:
        angulo = 180-180/numero_de_picos 
    print("Escoja dos colores:")
    color1 = input("Color 1: ")
    color2 = input("Color 2: ")
    color(color1, color2)
    begin_fill()
    while True:
        forward(200)
        left(angulo)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
print(estrellas_personalizada())