# Taller 2 - Programación de computadores UNAL 2024-1
**Equipo**: Ingenieros Megatróficos

![logo](https://camo.githubusercontent.com/a12903c4e2f58575622e5cc1222df41a66748bec5311fb8b769d680428dbb9ff/68747470733a2f2f692e6962622e636f2f767652785072622f412d616469722d756e2d742d74756c6f2e706e67)

**Integrantes**: Julian Gustin, Kevin Castellanos y Lucas García.

*Nota*: Para esta actividad se utilizó Python 3.12.5
## Ejercicio 2
***
El objetivo era desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.

Para esto creamos una función donde al ingresar un número se guarden los digitos enteros en una lista y los decimales en otra.
```python
def num(x): # Funcion de Entero a Lista de Digitos
    k = []  # Lista Vacia a agregar Digitos Enteros
    l = []  # Lista Vacia a agregar Digitos Decimales

    # Se declaran e inicializan variables
    cantidadDecimales = int(input("¿Cuantos decimales tiene el numero?"))
    digitosEnteros = int(x)
    digitosDecimales = x - digitosEnteros
    digitosDecimales = int(digitosDecimales*10**cantidadDecimales)

    # Separacion en 2 listas para los digitos enteros y los decimales

    while digitosEnteros > 0:  # para evitar problemas se toman valores positivos
        dg = digitosEnteros % 10  # se toma el ultimo digito, que es el residuo del cociente
        k.insert(0, dg) # se agrega a la lista
        digitosEnteros = digitosEnteros // 10 # se hace la division entera para borrar el ultimo decimal

    while digitosDecimales > 0:  # para evitar problemas se toman valores positivos
        dg = digitosDecimales % 10  # se toma el ultimo digito, que es el residuo del cociente
        l.insert(0, dg) # se agrega a la lista
        digitosDecimales = digitosDecimales // 10 # se hace la division entera para borrar el ultimo decimal
    return k, l # se regresan ambas listas
```
Hecho esto ya se ejecuta el código, se llama la función y se imprimen resultados.
```python

def fin(a, enteros, decimales): # Funcion para imprimir resultados
    print(f"Del numero {a} se tiene que:")
    print(f"{enteros} son los digitos enteros y {decimales} los decimales")

if __name__ == "__main__": # Funcion main para iniciar el codigo
    # Se pide el valoor de a y se llama a la funcion para separar sus digitos
    a = float(input("Tu numero es: ")) 
    enteros, decimales = num(a)
    fin(a,enteros,decimales)
```
## Ejercicio 3 (Números Espejos)
***
Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.
```python
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
```
## Ejercicio 5
***
La idea era desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros, abordando el problema desde una perpectiva tanto iterativa como recursiva.

Para esto se utilizó el Algoritmo de Euclides para el cálculo del Máximo Común Divisor.
### Caso Iterativo:
```python
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
```
### Caso Recursivo:
```python
def mcd_recursivo(a, b): # Funcion para hallar el mcd por recursion
    # Se reorganiza para que a siempre sea mayor que b
    if a < b: 
        a, b = b, a
    # Se termina el bucle cuando b sea igual a 0 y se retorna a como MCD
    if b == 0:
        return a
    return mcd_recursivo(b, a % b) # Se llama denuevo la funcion con a=b y b = al modulo de a y b
```
Luego se utilizó la relación del MCM Y MCD, es decir:
```python
def funcionMcm(mcd,a,b): # Funcion para hallar el mcm
    # Se halla mediante la relacion de que: mcm*mcd = a*b
    mcm = (a*b) // mcd
    return mcm
```
Finalmente se ejecuta el código, se llaman las funciones y se imprimen los resultados:
```python
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
```
## Ejercicio 6
***
Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in.
```python
def m(): # Funcion para Ingresar Una Lista
    l = [] # Lista a almacenar valores
    while True: # Bucle para agregar digitos sin limite previo 
        k = input(f"Ingrese el elemento {len(l) + 1} (o presione Enter para terminar): ") # se ingresan digitos hasta que el usuario desee
        if k == '':
            break
        l.append(k) #see agrega los valores a la lista
    return l # retorna la lista 

def j(p): # Funcion contadora de repeticiones
    k = [] # lista vacia para almacenar los valores que se repiten
    for i in p: # se agrega a la lista los valores que se repitan y que no esten en dicha lista
        if p.count(i) > 1 and k.count(i) == 0:
             k.append(i)
    for i in k: # se imprime los valores que se repiten junto con la cantidad de veces que se repite
        print(f"{i} se repite {p.count(i) - 1} veces")
    
if __name__ == "__main__":
    print("Lista: ")
    q = m()
    z = j(q)
```
## Ejercicio 8
***
Se trabajó en desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.

Por lo que primero creamos una función para crear ambas listas.
``` python
def crearLista()-> list: # Funcion para crear una lista
    # Declaracion de variables locales
    lista1: list = []
    lista2: list = []
    bandera: bool = True
    while bandera == True: # Ciclo infinito hasta que se de el break
        # Ciclo para agregar los elementos deseados a cada lista
        elementos = input(f"Para la lista 1 ingrese el elemento {len(lista1) + 1} (o presione Enter para terminar): ")
        if elementos == '': # Condicion para romper el ciclo
            break
        lista1.append(elementos)
    print(f"la primera: {lista1}")
    while bandera == True: # Ciclo infinito hasta que se de el break
        # Ciclo para agregar los elementos deseados a cada lista
        elementos = input(f"Para la lista 2 ingrese el elemento {len(lista2) + 1} (o presione Enter para terminar): ")
        if elementos == '': # Condicion para romper el ciclo
            break
        lista2.append(elementos)
    print(f"la segunda: {lista2}")
    return lista1, lista2
```
Luego comparamos cada elemento de la primer lista para ver si se repetia dentro de la segunda.
``` python
def compararListas(lista1: list, lista2: list)-> list: # Funcion para comparar listas
    salida: list = [] # Declaracion de variable
    for i in range(len(lista1)): # Ciclo para cada elemento unico en lista1 sea agregado a lista3
        if (lista1[i] in lista2) == False:
            salida.append(lista1[i])
    return salida
```
Finalmente se ejecuta el código, se llaman las funciones y se imprimen los resultados.
```python
def fin(): # Funcion para imprimir resultados
    print("Los elementos de la lista 1 que no estan en la lista 2 son:")
    print(lista3)
                   
if __name__ == "__main__": # Funcion main para indicar el inicio del codigo
    # Instrucciones iniciales
    print("Obtengamos elementos unicos en la lista 1")

    # Creacion de listas
    print("Crea ambas listas")
    lista1, lista2 = crearLista()

    # Comparacion de listas
    lista3: list = compararListas(lista1, lista2)
    fin()
```
## Ejercicio 9

Escriba un programa que pida 5 Vectores y calcule las siguientes operaciones:
El promedio, La mediana, El promedio multiplicativo, Ordenar los números de forma ascendente y descendente, La potencia del mayor número elevado al menor número y la raíz cúbica del menor número
```python
def m(b): 
    # Función generadora de vectores
    l = []  # Inicializa un vector vacía
    while True:
        # Solicita al usuario que ingrese un elemento para el vector
        k = input(f"Ingrese el elemento {len(l) + 1} de el vector {b} (presione Enter para continuar con la siguiente vector): ")
        if k == '': 
            # Si el usuario no ingresa un valor, se termina la entrada de elementos para el vector actual
            break
        l.append(float(k)) 
        # Agrega el valor ingresado convertido a float a el vector
    return l 
    # Retorna el vector creado

def prm(*args): 
    # Calcula el promedio de los vectores ingresados
    k = []  # Inicializa un vector para almacenar los promedios
    for j in range(len(args[0])): 
        # Itera sobre la longitud de la primera vector en args (asume que todas los vectores tienen la misma longitud)
        x = 0
        for i in args:
            # Suma los elementos en la misma posición de cada vector
            x += i[j]
        k.insert(j, x / len(args)) 
        # Calcula el promedio y lo inserta en la posición correspondiente
    return k 
    # Retorna el vector con los promedios

def med(a, b, c, d, e): 
    # Calcula la mediana de los vectores ingresadas
    q = []  # Inicializa un vector para almacenar las medianas
    p = len(a)  # Longitud de los vectores (se asume que todas tienen la misma longitud)
    l = p // 2  # Calcula el índice del valor central
    for i in range(p): 
        # Itera sobre la longitud de los vectores
        k = [a[i], b[i], c[i], d[i], e[i]] 
        # Crea un vector con los elementos en la posición i de cada vector
        k.sort() 
        # Ordena el vector k
        q.append(k[l]) 
        # Agrega el valor medio (mediana) a el vector q
    return q 
    # Retorna el vector con las medianas

def prmx(*args): 
    # Calcula el promedio geométrico de los vectores ingresadas
    k = []  # Inicializa un vector para almacenar los promedios geométricos
    for j in range(len(args[0])): 
        # Itera sobre la longitud del primer vector
        x = 1
        for i in args:
            # Multiplica los elementos en la misma posición de cada vector
            x *= i[j]
        k.append(x ** (1 / len(args))) 
        # Calcula la raíz enésima del producto (promedio geométrico) y la agrega a k
    return k 
    # Retorna el vector con los promedios geométricos

def ord(*args): 
    # Ordena los vectores de menor a mayor
    for i in args:
        i.sort() 
        # Ordena cada vector individualmente
    print("vectores ordenadas de menor a mayor:")
    for i in args:
        print(i) 
        # Imprime cada vector ordenado

def ordx(*args): 
    # Ordena los vectores de mayor a menor
    for i in args:
        i.sort(reverse=True) 
        # Ordena cada vector individualmente en orden inverso
    print("vectores ordenadas de mayor a menor:")
    for i in args:
        print(i) 
        # Imprime cada vector ordenado

def mmx(*args): 
    # Calcula el máximo de cada vector elevado al mínimo de la misma vector
    k = []  # Inicializa un vector para almacenar los resultados
    for i in args:
        l = max(i) ** min(i) 
        # Calcula el máximo elevado al mínimo y lo almacena en l
        k.append(l) 
        # Agrega el resultado a el vector k
    return k 
    # Retorna el vector con los resultados

def minx(*args): 
    # Calcula la raíz cúbica del mínimo de cada vector
    k = []  # Inicializa un vector para almacenar los resultados
    for i in args:
        l = min(i) ** (1/3) 
        # Calcula la raíz cúbica del mínimo y lo almacena en l
        k.append(l) 
        # Agrega el resultado a el vector k
    return k 
    # Retorna el vector con los resultados

if __name__ == "__main__":
    # Ejecuta las 5 vectores 
    p = m(1)  
    q = m(2)  
    r = m(3)  
    s = m(4)  
    t = m(5)  
    
    z = prm(p, q, r, s, t)  # Calcula el promedio de los vectores
    k = med(p, q, r, s, t)  # Calcula la mediana de los vectores
    l = prmx(p, q, r, s, t)  # Calcula el promedio geométrico de los vectores
    i = minx(p, q, r, s, t)  # Calcula la raíz cúbica del menor número en cada vector
    c = mmx(p, q, r, s, t)  # Calcula el máximo elevado al mínimo en cada vector
    
    # Imprime los resultados
    print("Promedio:", z)
    print("Mediana:", k)
    print("Promedio geométrico:", l)
    ord(p, q, r, s, t)  # Ordena los vectores de menor a mayor
    ordx(p, q, r, s, t)  # Ordena los vectores de mayor a menor
    print("Máximo elevado al mínimo:", c)
    print("Raíz cúbica del menor número:", i)
```
