# Taller 2 - Programación de computadores UNAL 2024-1
Equipo: Ingenieros Megatróficos

(Inserten logo)

Integrantes: Julian Gustin, Kevin Castellanos y Lucas García.

Nota: Para esta actividad se utilizó Python 3.12.5
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
## Ejercicio 3
***
```python
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
```python
def m():
    l = []
    while True:
        k = input(f"Ingrese el elemento {len(l) + 1} (o presione Enter para terminar): ")
        if k == '':
            break
        l.append(k)
    return l

def r(p):
    for x in range(len(p)):
        for y in range(x+1,len(p)):
          if p[x] == p[y]:
           print(p[x]," es repetido ", p.count(p[x]) - 1 , " veces" )
           
           
if __name__ == "__main__":
    print("Lista: ")
    q = m()
    z = r(q)
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
***
```python
def m():
    l = []
    while True:
        k = input(f"Ingrese el elemento {len(l) + 1} de la lista (o presione Enter para terminar): ")
        if k == '':
            break
        l.append(float(k))
    return l

def prm(*args):
    k = []
    for j in range(len(args[0])):
        x = 0
        for i in args:
            x += (i[j])
        k.insert(j, x/len(args))
    return k

def med(a,b,c,d,e):
    q = []
    p = len(a)
    l = p//2
    for i in range(p):
        k = [a[i], b[i], c[i], d[i], e[i]]
        k.sort()
        q.append(k[l])
    return q

def prmx(*args):
    k = []
    for j in range(len(args[0])):
        x = 1
        for i in args:
            x *= (i[j])
        k.insert(j, x**1/(len(args)))
    return k

def ord(*args):
    for i in args:
        i.sort()
    print("Listas ordenadas de menor a mayor:")
    for i in args:
        print(i)

def ordx(*args):
    for i in args:
        i.sort(reverse=True)
    print("Listas ordenadas de mayor a menor:")
    for i in args:
        print(i)

def mmx(*args):
    k = []
    for i in args:
        l = max(i)**min(i)
        k.append(l)
    return print(k)

def minx(*args):
    k = []
    for i in args:
     l = min(i)**(1/3)
     k.append(l)
    return k

if __name__ == "__main__":
    p = m()
    q = m()
    r = m()
    s = m()
    t = m()
    
    z = prm(p, q, r, s, t)
    k = med(p, q, r, s, t)
    l = prmx(p, q, r, s, t)
    i = minx(p, q, r, s, t)
   

    print("Promedio", z)
    print("Mediana:", k)
    print("Promedio geométrico:", l)
    ord(p, q, r, s, t)
    ordx(p, q, r, s, t)
    mmx(p, q, r, s, t)
    print("raiz cubica del menor numero", i)
```
