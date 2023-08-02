def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

def generar_matriz(filas, columnas):
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    return matriz


filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))


matriz_generada = generar_matriz(filas, columnas)
print("Matriz generada:")
imprimir_matriz(matriz_generada)