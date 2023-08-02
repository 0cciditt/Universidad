import random

def generar_lista_aleatoria(longitud):
    lista_aleatoria = [random.randint(1, 100) for _ in range(longitud)]
    return lista_aleatoria


longitud_lista = int(input("Ingrese la longitud de la lista: "))


lista_aleatoria = generar_lista_aleatoria(longitud_lista)
print("Lista aleatoria generada:", lista_aleatoria)
