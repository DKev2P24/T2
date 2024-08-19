def num(x): # Funcion de Entero a Lista de Digitos
    k = []  # Lista Vacia a agregar digitos
    while x > 0:  # para evitar problemas se toman valores positivos
        dg = x % 10  # se toma el ultimo digito, que es el residuo del cociente
        k.insert(0, dg) # Se agrega el elemento a la primera posición de una lista
        x = x // 10 # se toma el valor resultante de la division entera para continuar, asi hasta el ultimo digito
    return k # regresa la lista con su numero espejo

def esp(x, y):
    # Verificar si ambos tienen la misma longitud
    if len(x) != len(y):
        print("No son espejos.")
        return

    # Comparar cada dígito
    for i in range(len(x)):
        if x[i] != y[len(x) - 1 - i]:
            print("No son espejos.")
            return
    
    # Si pasa todas las comparaciones, son espejos
    print("Son Espejos.")
    
if __name__ == "__main__":
    a = int(input("A: ")) # se ingresan los valores y se llaman a las funciones, respectivamente
    b = int(input("B: "))
    x = num(a)
    y = num(b)
    z = esp(x,y)
    print(x)
    print(y)