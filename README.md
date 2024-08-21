# Taller 2 - Programación de computadores UNAL 2024-1
**Equipo**: Ingenieros Megatróficos

![logo](https://i.ibb.co/440n654/A-adir-un-t-tulo.png)

**Integrantes**:
- Julian Gustin 
- Kevin Castellanos T.I. 1052338203
- Lucas García T.I. 1062434165

*Nota*: Para esta actividad se utilizó Python 3.12.5
## Ejercicio 1
***
Desarrollar un programa que ingrese un número entero n y separe todos los digitos que lo componen.
Para lograr este objetivo, se usaron los operadores % (Modulo) y // (División entera), el operador de modulo permite obtener el ultimo digito de un numero, pues al hacer modulo con 10, el residuo siempre será el ultimo digito del numero entero proporcionado.
La división entera con 10 sirve para eliminar el ultimo digito, ya que similarmente al proceso con el operador de modulo, se obtiene la división entera sin el residuo. Al repetir este proceso, se obtienen todos los digitos y se los añade al final de una lista que después es revertida. Este proceso se repite mientras que n sea mayor a 0
```python
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
```

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
## Ejercicio 4
**
Calcular la aproximación a la funcion coseno alrededor de 0 para cualquier x real usando la serie de Taylor.
Para conseguir este objetivo, se usaron distintas funciones para que el codigo tenga más orden y se las pueda llamar cuando se ejecute main.
Primero se definen 2 funciones base, la de valor absoluto y la factorial, esto para evitar usar las funciones que incluye math, aunque ambas opciones son validas. 
```python
def valor_absoluto(n): #Definir función de valor absoluto
    if n >= 0:
        return n
    else:
        return -n
    
def factorial(n): #Definir función factorial (Copiada de retos anteriores)
    resultado = 1
    for i in range(1, (n+1)):
        resultado *= i 
    return resultado
```
Luego se procede a definir la funcion de aproximación al coseno, usando la serie de Taylor proporcionada en el ejercicio, se llama a la función factorial para el numerador. Se itera n veces, teniendo en cuenta que n sera el numero de iteraciones que obtendremos después mediante la funcion de error.
```python
def coseno_taylor(x,n): #Calcular la aproximación de coseno utilizando n terminos de la serie de taylor
    cos_aprox = 0 #Inicializar la aproximación del coseno en 0
    for i in range(n): #Itera desde 0 hasta n-1
        termino = ((-1)**i)*(x**(2*i)) / factorial(2*i) #Calcular el termino i de la serie de taylor
        cos_aprox += termino #Suma el termino actual a la aproximación del coseno
    return cos_aprox 
```
Para calcular el porcentaje de error relativo, se debe calcular el valor real del coseno usando math. Para mayor orden, se hacen dos listas, una de ellas con las tolerancias que buscamos, y otra que almacenará los resultados de n y los de error.
Se usa la función de valor absoluto para obtener porcentajes positivos.
```python
def calcular_error(x): #Calcular los errores para distintos valores de n en la serie
    cos_real = math.cos(x) #Calcula el coseno real
    errores = [0.1, 0.01, 0.001, 0.0001] #Lista de tolerancias a evaluar
    resultado = [] #Lista para almacenar resultados
    for tolerancia in errores: #Itera sobre cada tolerancia en la lista
        n=0
        while True: #Bucle que se rompe cuando se encuentra n
            n+=1 #Incrementa n en cada iteración
            cos_aprox = coseno_taylor(x,n) #Calcula el coseno aproximado
            error = valor_absoluto((cos_real - cos_aprox)/cos_real) #Calcula el error entre la aproximación y valor real, se usa valor absoluto para obtener resultados positivos
            if error <= tolerancia:
                resultado.append((n, tolerancia, error)) #Cuando el error sea menor o igual a la tolerancia, almacena n y el error en la lista de resultados
                break 
    return resultado
```
Finalmente, se llama a todas estas funciones y se imprime el valor real del coseno, el numero de iteraciones necesarias para cada tolerancia y el valor aproximado de la funcion para cada número de iteraciones.
```python
if __name__ == "__main__":
    x = float(input("Ingrese un número real x menor a 30: ")) #Solicita al usuario ingresar el valor de x, tiene que ser menor a 30 porque el programa ya no funciona con factoriales más grandes a este.
    cos_real = math.cos(x)
    print(f"El valor real de la funcion coseno en x es {cos_real}") 
    resultado = calcular_error(x) 
    for n, tolerancia, error in resultado: #Calcula la aproximación con el numero de terminos encontrado.
        cos_aprox = coseno_taylor(x,n) 
        print(f"Para un error de {tolerancia*100}% se necesita un n = {n}")
        print(f"Valor de cos aproximado con {n} iteraciones ≈ {cos_aprox}, con un error de {error*100}%")
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
## Ejercicio 7
***
Determinar si en una lista existe una cadena de caracteres con dos o más vocales e imprimirla, si no existe no se imprime.
Se define primero la función para contar las vocales en una cadena, lo hace mediante un bucle for para cada caracter, añadiendo uno si encuentra una vocal. Para esto se define primero una cadena con todas las vocales en minusculas y mayusculas. Si el contador es igual o mayor a 2, retorna un valor booleano True, de lo contrario retorna false.
```python
def contiene_vocales(cadena:str): #Función para verificar si una cadena tiene dos o más vocales
    vocales = "aeiouAEIOU" #Define todas las vocales en minúsculas y mayúsculas para verificar si los caracteres en una cadena son vocales
    conteo_vocales = 0 #Inicia el contador de vocales
    for char in cadena: #Itera sobre cada caracter de la cadena
        if char in vocales: #Si el caracter es una vocal, añade 1 al contador
            conteo_vocales +=1
    return conteo_vocales >= 2 #Retornea True si el conteo es de 2 o más o false en caso contrario.
```
Posteriormente, se define una función que busca cadenas que tengan 2 o más vocales en una lista usando un ciclo for. Usa una bandera "encontrado" para que imprima todas las cadenas que cumplan con el requisito, de lo contrario solo imprimiría la primera. Si no existe ninguna, imprime "No existe
```python
def buscar_cadena_vocales(lista:str): #Busca las cadenas que cumplan el requisito
    encontrado = False #Bandera para saber si una cadena cumple con el requisito 
    for cadena in lista: #Para todas las cadenas en la lista
        if contiene_vocales(cadena): #Si cumple con el requisito, cambia el booleano a True y la imprime.
            print(cadena)
            encontrado = True
    if not encontrado: #Si no existe ninguna, imprime "No existe"
        print("No existe")
```
Finalmente, se inicia main y se llama a las funciones, no sin antes usar un bucle for para que el usuario ingrese 3 palabras, y estas se añadan al final de una lista de cadenas. 
```python
if __name__ == "__main__":
    lista_cadenas = [] #Lista de cadenas donde se ingresarán las palabras del usuario.
    for i in range(3): #Ingresar 3 palabras y añadirlas a la lista de cadenas
        palabra = input(f"Ingresa la palabra {i+1}: ")
        lista_cadenas.append(palabra)
    buscar_cadena_vocales(lista_cadenas) #Busca cadenas con 2 vocales o más
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
## Ejercicio 10
Se desarrolló una función que al ingresar una lista "A", independientemente de los números que se encuentran en esta, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función.

Para esto, se requirió resolver el problema desde dos perspectivas:
### Usando un patrón de acumulación
```python
# Se ingresa la lista A y retorna la lista de múltiplos
def MultiplosDe3(listaA: list)-> list:
    listaMultiplos: list = []
    for i in range(0, len(listaA)): # Se comprueba cada elemento para saber si es múltiplo de 3 y agregarlo a la lista
        if listaA[i] % 3 == 0:
            listaMultiplos.append(listaA[i])
    return listaMultiplos
```
### Usando comprensión de listas
```python
# Se ingresa la lista A y retorna la lista de múltiplos
def MultiplosDe3(listaA: list)-> list: 
    # Harán parte de la lista de múltiplos todos los elementos de la lista A que su residuo al dividirse entre 3 sea 0
    listaMultiplos: list = [listaA[i] for i in range(0,len(listaA)) if listaA[i] % 3 == 0]
    return listaMultiplos
```
### Finalmente
Se planteó el desafio de analizar estos múltiplos de 3 en la lista A sin utilizar el operador "%", lo cuál se realizó de la siguiente forma:

```python
# Se ingresa la lista A y retorna la lista de múltiplos
def MultiplosDe3(listaA: list)-> list:

    # Se declaran e inicializan variables 
    listaMultiplos: list = []
    i : int = 0
    j : int = 0
    for i in range(0,len(listaA)): # Ciclo para todos los elementos de la lista A
        h : int = 0
        n : int = 0
        dg : int = 0
        x : int = abs(listaA[i]) # Se toma el valor absoluto para extraer los dígitos sin problemas de un número negativo
        listaDeDigitos: list = []
        if x == 0: # Caso puntual del elemento 0 que es múltiplo común
            listaMultiplos.append(listaA[i])

        # Mientras x sea un número entero positivo
        while x > 0:
            # Se toma el residuo al dividirse entre 10 y ese valor se agrega a la lista de digitos
            dg = x % 10
            listaDeDigitos.insert(0,dg)
            x //= 10

        # Patrón de acumulación para sumar los digitos del elemento actual    
        for j in range(0,len(listaDeDigitos)):
            n += listaDeDigitos[j]

        # Ciclo para agregar aquellos elementos cuya suma de sus digitos sea un múltiplo de 3
        while h < 10*len(listaDeDigitos): # Se itera la condición hasta que el factor de 3 sea mayor a 10 veces la cantidad de digitos
            if n == 3*h:
                listaMultiplos.append(listaA[i])
            h += 1
    return listaMultiplos
```
Y este es el código en general para crear la lista A, y con el método preferido se obtendrán los múltiplos que se mostrarán en la terminal.
```python
def crearLista()-> list: # Funcion para Ingresar Una Lista
    l : list= [] # Lista a almacenar valores
    while True: # Bucle para agregar digitos sin limite previo 
        try:
            k = int(input(f"Ingrese el elemento {len(l) + 1} (o presione Enter para terminar): ")) # Se ingresan cuantos elementos se desee
        except ValueError:
            break # Se rompe el ciclo cuando se ingresa un valor incorrecto
        l.append(k) # se agrega a l
    return l # retorna la lista 

def Resultados(Multiplos: list): # Se imprimen resultados
    print(f"De la lista ingresada {listaA}, los números múltiplos de 3 son:")
    print(Multiplos)

if __name__ == "__main__": # Funcion main para indicar el inicio del codigo
    # Se utilizan las tres funciones
    listaA = crearLista()
    Multiplos = MultiplosDe3(listaA)
    Resultados(Multiplos)
```
## Ejercicio 11
Algoritmo para identificar si una matriz cuadrada es mágica.
Una matriz es magica cuando la suma de todas sus filas, columnas y diagonales es la misma. Para saber esto, usamos una función que primero identifique si la matriz es cuadrada, identificando si cada linea tiene n elementos.
```python
def matriz_magica(matriz):
    n = len(matriz) #Obtener el tamaño de la matriz
    for fila in matriz:
        if len(fila) !=n: #Si una fila no tiene n elementos, no es cuadrada
            return False
```
Posteriormenete, se suma la primera fila para tener una referencia.
```python
  suma_ref = 0 
    for elemento in matriz[0]: #Se indexa desde 0
        suma_ref += elemento #Suma la primera fila como referencia
```
La suma de las filas es la más sencilla, pues se suma cada elemento de la lista con un ciclo for.
```python
    for fila in matriz: #Comprueba la suma de cada fila
        sumar_fila = 0
        for elemento in fila:
            sumar_fila += elemento #Suma cada elemento de la fila
        if sumar_fila != suma_ref: #Si es distinta a la de referencia, retorna falso
            return False
```
Para sumar las columnas, se indexa la matriz con [fila][columna] para obtener la columna actual
```python
    for columna in range(n): #Comprueba la suma de cada columna
        sumar_columna = 0
        for fila in range(n):
            sumar_columna += matriz[fila][columna] #Suma los elementos de la columna actual
        if sumar_columna != suma_ref: #Si es distinta a la de referencia, retorna falso
            return False
```
Para la suma de las diagonales, se indexa de forma [i][i] para la primera para obtener parejas en diagonal, y para la otra diagonal, cambia la segunda indexación, ya que se debe recurrir al penultimo elemento de la fila [n - i - 1] se resta -1 porque se indexa desde 0
Todos estos resultados se comparan con la suma de referencia, y retorna true si cumple con los requisitos y false en caso contrario.
```python
  sum_diag_1 = 0 #Suma los elementos de la diagonal de izquierda a derecha
    for i in range(n):
        sum_diag_1 += matriz[i][i] #Elementos de la diagonal principal, en este caso, 0,0 (esquina superior izquierda) 1,1 (fila 2 columna 2), etc.
    if sum_diag_1 != suma_ref:
        return False
    
    sum_diag_2 = 0 #Suma los elementos de la diagonal de derecha a izquierda
    for i in range(n):
        sum_diag_2 += matriz[i][n - i - 1] #La indexación de filas sigue igual, pero para las columnas, se incia desde la esquina superior derecha, que sería n - i - 1 (porque se indexa desde 0)
    if sum_diag_2 != suma_ref:
        return False
    
    return True #Retorna verdadero si cumple con todo
```
Al final, se usan ciclos for para crear una matriz con input del usuario, escribiendo fila por fila y añadiendolas a la matriz.
```python
def crear_matriz():
    n = int(input("Ingresa el tamaño de la matriz (cuadrada): "))  #Lee el tamaño de la matriz
    matriz = []  
    for i in range(n):
        fila = []  #Inicializa una lista para la fila actual
        for j in range(n):
            elemento = int(input(f"Elemento [{i+1}][{j+1}]: ")) #Lee el elemento de la posición [i][j] y lo agrega a la fila
            fila.append(elemento)  
        matriz.append(fila) #Agrega la fila a la matriz
    print("La matriz es:")
    for fila in matriz:
        print(fila) #Imprime las filas de la matriz
    return matriz 
```
Finalmente, se llama a las funciones y se comprueba.
```python
if __name__ == "__main__":
    matriz = crear_matriz()
    if matriz_magica(matriz):
        print("La matriz es magica")
    else:
        print("La matriz no es magica")
```
