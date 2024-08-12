# T2
Taller 2 
## Ejercicio 2
```python
def num(x): # Funcion de Entero a Lista de Digitos
    k = []  # Lista Vacia a agregar Digitos Enteros
    l = []  # Lista Vacia a agregar Digitos Decimales

    cantidadDecimales = int(input("¿Cuantos decimales tiene el numero?"))
    digitosEnteros = int(x)
    digitosDecimales = x - digitosEnteros
    digitosDecimales = int(digitosDecimales*10**cantidadDecimales)

    while digitosEnteros > 0:  # para evitar problemas se toman valores positivos
        dg = digitosEnteros % 10  # se toma el ultimo digito, que es el residuo del cociente
        k.insert(0, dg) 
        digitosEnteros = digitosEnteros // 10

    while digitosDecimales > 0:  # para evitar problemas se toman valores positivos
        dg = digitosDecimales % 10  # se toma el ultimo digito, que es el residuo del cociente
        l.insert(0, dg) 
        digitosDecimales = digitosDecimales // 10
    return k, l

def fin(a, enteros, decimales):
    print(f"Del numero {a} se tiene que:")
    print(f"{enteros} son los digitos enteros y {decimales} los decimales")

if __name__ == "__main__":
    a = float(input("Tu numero es: "))
    enteros, decimales = num(a)
    fin(a,enteros,decimales)
```
## Ejercicio 3
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
```python
def mcd_iteracion(a,b):
    if a < b:
        a, b = b, a
    if a == b:
        MCD = a
        return MCD
    else:
        while a >= b:
            residuo = a - b
            if residuo == 0:
                return a
            a = residuo
            if a < b:
                a, b = b, a
def mcd_recursivo(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return mcd_recursivo(b, a % b)

def funcionMcm(mcd,a,b):
    mcm = (a*b) // mcd
    return mcm
def fin (mcd,mcm,a,b):
    print(f"Y ya que el máximo común divisor es {mcd}, entonces:")
    print(f"El mínimo común multiplo es igual a {mcm}")

if __name__ == "__main__":
    print("Digita dos numeros enteros para hallar su MCM")
    a = int(input("El primero:"))
    b = int(input("El segundo:"))
    mcd = mcd_iteracion(a,b)
    mcd2 = mcd_recursivo(a,b)
    print(f"MCD por iteración: {mcd}, por recursion: {mcd2}, es decir, el mismo resultado")
    mcm = funcionMcm(mcd,a,b)
    fin(mcd,mcm,a,b)
```
## Ejercicio 6
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
## Ejercicio 9
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
