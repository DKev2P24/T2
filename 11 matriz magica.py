def matriz_magica(matriz):
    n = len(matriz) #Obtener el tamaño de la matriz
    for fila in matriz:
        if len(fila) !=n: #Si una fila no tiene n elementos, no es cuadrada
            return False
        
    suma_ref = 0 
    for elemento in matriz[0]: #Se indexa desde 0
        suma_ref += elemento #Suma la primera fila como referencia


    for fila in matriz: #Comprueba la suma de cada fila
        sumar_fila = 0
        for elemento in fila:
            sumar_fila += elemento #Suma cada elemento de la fila
        if sumar_fila != suma_ref: #Si es distinta a la de referencia, retorna falso
            return False
        

    for columna in range(n): #Comprueba la suma de cada columna
        sumar_columna = 0
        for fila in range(n):
            sumar_columna += matriz[fila][columna] #Suma los elementos de la columna actual
        if sumar_columna != suma_ref: #Si es distinta a la de referencia, retorna falso
            return False

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

if __name__ == "__main__":
    matriz = crear_matriz()
    if matriz_magica(matriz):
        print("La matriz es magica")
    else:
        print("La matriz no es magica")


