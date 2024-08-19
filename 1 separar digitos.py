def separar_digitos(n:int)->int: #Definir función que separa los digitos
    digitos = [] #Definir lista de digitos
    while n > 0:
        digito = n % 10 #Obtiene el ultimo digito
        digitos.append(digito) #Agrega el digito al final de la lista
        n = n//10 #Elimina el ultimo digito del numero
    digitos.reverse() #Invierte la lista para obtener el orden correcto
    return digitos #Devuelve la lista

if __name__ == "__main__":
    n = int(input("Ingrese un número entero: ")) #Solicita el número entero al usuario
    digitos = separar_digitos(n) #Aplica la función al numero n
    print(f"Los digitos del número {n} son {digitos}") #Imprime la lista de los digitos separados.