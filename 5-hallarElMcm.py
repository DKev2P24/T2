def mcd_iteracion(a,b): # Funcion para hallar el mcd por iteracion
    # Se reorganiza para que a siempre sea mayor que b
    if a < b:
        a, b = b, a
    # Si son el mismo numero ellos mismos son el MCD
    if a == b:
        MCD = a
        return MCD
    else: # Caso comun donde a es mayor que b
        # Se realiza el Algoritmo de Euclides
        while a >= b:
            residuo = a - b
            # Cuando el residua sea 0, a sera el MCD y termina el bucle
            if residuo == 0:
                return a
            a = residuo
            if a < b:
                a, b = b, a

def mcd_recursivo(a, b): # Funcion para hallar el mcd por recursion
    # Se reorganiza para que a siempre sea mayor que b
    if a < b: 
        a, b = b, a
    # Se termina el bucle cuando b sea igual a 0 y se retorna a como MCD
    if b == 0:
        return a
    return mcd_recursivo(b, a % b) # Se llama denuevo la funcion con a=b y b = al modulo de a y b

def funcionMcm(mcd,a,b): # Funcion para hallar el mcm
    # Se halla mediante la relacion de que: mcm*mcd = a*b
    mcm = (a*b) // mcd
    return mcm

def fin (mcd,mcm,a,b): # Funcion para imprimir resultados
    print(f"Y ya que el máximo común divisor es {mcd}, entonces:")
    print(f"El mínimo común multiplo es igual a {mcm}")

if __name__ == "__main__": # Funcion main para iniciar el codigo
    # Instrucciones e ingreso de los numeros
    print("Digita dos numeros enteros para hallar su MCM")
    a = int(input("El primero:"))
    b = int(input("El segundo:"))

    # Se llaman a las funciones para hallar mcd por ambos metodos
    mcd = mcd_iteracion(a,b)
    mcd2 = mcd_recursivo(a,b)
    print(f"MCD por iteración: {mcd}, por recursion: {mcd2}, es decir, el mismo resultado")

    # Se halla el mcm con el resultado y se imprime
    mcm = funcionMcm(mcd,a,b)
    fin(mcd,mcm,a,b)