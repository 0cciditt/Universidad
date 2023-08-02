import math

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * radio ** 2
    return area

area_circulo = calcular_area_circulo()
print(f"El área del círculo es: {area_circulo}")