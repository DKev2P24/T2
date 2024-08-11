def num(x): # Funcion de Entero a Lista de Digitos
    k = []  # Lista VVacia a agregar Digitos
    while x > 0:  # para evitar problemas se toman valores positivos
        dg = x % 10  # se toma el ultimo digito, que es el residuo del cociente
        k.insert(0, dg) #
        x = x // 10
    return k

def esp(x,y):
    if len(x) != len(y):
        print("No son espejos. ")
        return
    
    for i in range(len(x)):
        if x[i] == y[len(x)-1-i]:
         print("Son Espejos")
        else:
         print("No son espejos")
        return
    
if __name__ == "__main__":
    a = int(input("A: "))
    b = int(input("B: "))
    x = num(a)
    y = num(b)
    z = esp(x,y)
    print(x)
    print(y)
