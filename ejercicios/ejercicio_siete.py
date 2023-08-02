mi_lista = [10, 5, 20, 15, 30]

def encontrar_maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

maximo, minimo = encontrar_maximo_minimo(mi_lista)

# Mostrar los resultados en la consola
print("El número más grande en la lista es:", maximo)
print("El número más pequeño en la lista es:", minimo)
