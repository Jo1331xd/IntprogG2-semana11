def convertir(numero):
    resultado= ""
    while numero > 0 :
        resto = numero % 2 
        resultado = str(resto) + resultado
        numero = numero // 2   

    return resultado

def main ():
    numero =int(input("Dime un numero "))

    if numero == 0:
        print(f"El numero en 0 su binario es: 0")
    
    elif numero > 0:
        binario=convertir(numero)
        print(f"El numero ingresado en binario es {binario}")
    else:
        print("El numero tiene que ser positivo")
main()