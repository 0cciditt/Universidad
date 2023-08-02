mi_lista = [10, 20, 30, 40, 50]


def calcular_media_aritmetica(lista):
    suma_total = sum(lista)
    media = suma_total / len(lista)
    return media



media_calculada = calcular_media_aritmetica(mi_lista)
print("La media aritmética de la lista es:", media_calculada)