def m(b): 
    # Función generadora de listas
    l = []  # Inicializa una lista vacía
    while True:
        # Solicita al usuario que ingrese un elemento para la lista
        k = input(f"Ingrese el elemento {len(l) + 1} de la lista {b} (presione Enter para continuar con la siguiente lista): ")
        if k == '': 
            # Si el usuario no ingresa un valor, se termina la entrada de elementos para la lista actual
            break
        l.append(float(k)) 
        # Agrega el valor ingresado convertido a float a la lista
    return l 
    # Retorna la lista creada

def prm(*args): 
    # Calcula el promedio de las listas ingresadas
    k = []  # Inicializa una lista para almacenar los promedios
    for j in range(len(args[0])): 
        # Itera sobre la longitud de la primera lista en args (asume que todas las listas tienen la misma longitud)
        x = 0
        for i in args:
            # Suma los elementos en la misma posición de cada lista
            x += i[j]
        k.insert(j, x / len(args)) 
        # Calcula el promedio y lo inserta en la posición correspondiente
    return k 
    # Retorna la lista con los promedios

def med(a, b, c, d, e): 
    # Calcula la mediana de las listas ingresadas
    q = []  # Inicializa una lista para almacenar las medianas
    p = len(a)  # Longitud de las listas (se asume que todas tienen la misma longitud)
    l = p // 2  # Calcula el índice del valor central
    for i in range(p): 
        # Itera sobre la longitud de las listas
        k = [a[i], b[i], c[i], d[i], e[i]] 
        # Crea una lista con los elementos en la posición i de cada lista
        k.sort() 
        # Ordena la lista k
        q.append(k[l]) 
        # Agrega el valor medio (mediana) a la lista q
    return q 
    # Retorna la lista con las medianas

def prmx(*args): 
    # Calcula el promedio geométrico de las listas ingresadas
    k = []  # Inicializa una lista para almacenar los promedios geométricos
    for j in range(len(args[0])): 
        # Itera sobre la longitud de la primera lista en args
        x = 1
        for i in args:
            # Multiplica los elementos en la misma posición de cada lista
            x *= i[j]
        k.append(x ** (1 / len(args))) 
        # Calcula la raíz enésima del producto (promedio geométrico) y la agrega a k
    return k 
    # Retorna la lista con los promedios geométricos

def ord(*args): 
    # Ordena las listas de menor a mayor
    for i in args:
        i.sort() 
        # Ordena cada lista individualmente
    print("Listas ordenadas de menor a mayor:")
    for i in args:
        print(i) 
        # Imprime cada lista ordenada

def ordx(*args): 
    # Ordena las listas de mayor a menor
    for i in args:
        i.sort(reverse=True) 
        # Ordena cada lista individualmente en orden inverso
    print("Listas ordenadas de mayor a menor:")
    for i in args:
        print(i) 
        # Imprime cada lista ordenada

def mmx(*args): 
    # Calcula el máximo de cada lista elevado al mínimo de la misma lista
    k = []  # Inicializa una lista para almacenar los resultados
    for i in args:
        l = max(i) ** min(i) 
        # Calcula el máximo elevado al mínimo y lo almacena en l
        k.append(l) 
        # Agrega el resultado a la lista k
    return k 
    # Retorna la lista con los resultados

def minx(*args): 
    # Calcula la raíz cúbica del mínimo de cada lista
    k = []  # Inicializa una lista para almacenar los resultados
    for i in args:
        l = min(i) ** (1/3) 
        # Calcula la raíz cúbica del mínimo y lo almacena en l
        k.append(l) 
        # Agrega el resultado a la lista k
    return k 
    # Retorna la lista con los resultados

if __name__ == "__main__":
    # Ejecuta las 5 listas 
    p = m(1)  
    q = m(2)  
    r = m(3)  
    s = m(4)  
    t = m(5)  
    
    z = prm(p, q, r, s, t)  # Calcula el promedio de las listas
    k = med(p, q, r, s, t)  # Calcula la mediana de las listas
    l = prmx(p, q, r, s, t)  # Calcula el promedio geométrico de las listas
    i = minx(p, q, r, s, t)  # Calcula la raíz cúbica del menor número en cada lista
    c = mmx(p, q, r, s, t)  # Calcula el máximo elevado al mínimo en cada lista
    
    # Imprime los resultados
    print("Promedio:", z)
    print("Mediana:", k)
    print("Promedio geométrico:", l)
    ord(p, q, r, s, t)  # Ordena las listas de menor a mayor
    ordx(p, q, r, s, t)  # Ordena las listas de mayor a menor
    print("Máximo elevado al mínimo:", c)
    print("Raíz cúbica del menor número:", i)

