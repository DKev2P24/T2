def contiene_vocales(cadena:str): #Función para verificar si una cadena tiene dos o más vocales
    vocales = "aeiouAEIOU" #Define todas las vocales en minúsculas y mayúsculas para verificar si los caracteres en una cadena son vocales
    conteo_vocales = 0 #Inicia el contador de vocales
    for char in cadena: #Itera sobre cada caracter de la cadena
        if char in vocales: #Si el caracter es una vocal, añade 1 al contador
            conteo_vocales +=1
    return conteo_vocales >= 2 #Retornea True si el conteo es de 2 o más o false en caso contrario.

def buscar_cadena_vocales(lista:str): #Busca las cadenas que cumplan el requisito
    encontrado = False #Bandera para saber si una cadena cumple con el requisito 
    for cadena in lista: #Para todas las cadenas en la lista
        if contiene_vocales(cadena): #Si cumple con el requisito, cambia el booleano a True y la imprime.
            print(cadena)
            encontrado = True
    if not encontrado: #Si no existe ninguna, imprime "No existe"
        print("No existe")

if __name__ == "__main__":
    lista_cadenas = [] #Lista de cadenas donde se ingresarán las palabras del usuario.
    for i in range(3): #Ingresar 3 palabras y añadirlas a la lista de cadenas
        palabra = input(f"Ingresa la palabra {i+1}: ")
        lista_cadenas.append(palabra)
    buscar_cadena_vocales(lista_cadenas) #Busca cadenas con 2 vocales o más