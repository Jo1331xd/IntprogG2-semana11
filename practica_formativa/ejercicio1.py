def recibir():
    numero=int(input("Dame un numero para sacar su factorial: "))
    return numero

def main():
    factorial=1
    numero_entero=recibir()
    for i in range (1,numero_entero +1 ):
        anterior = factorial
        factorial= i * anterior 
        print(f"Factorial del numero !{i}= {anterior} x {i} = {factorial}") 
        if numero_entero <= 0: 
            print("El numero tiene que ser positivo")
        
main()