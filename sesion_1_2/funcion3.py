#Calcular el area de un circulo 
"""formula area pi * ( r * r )"""

import math

def calcular_area_circulo(radius):
    return math.pi * radius ** 2

def main():
    
    radius=int(input("Ingrese cuanto es el radio del circulo: "))
    area = calcular_area_circulo(radius)
    print(f"El area del circulo es: {area}")

main()