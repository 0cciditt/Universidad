def calcular_factorial(numero):
    if numero < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    elif numero == 0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

if __name__ == "__main__":
    try:

        numero_dado = int(input("Ingrese un número entero no negativo: "))


        factorial = calcular_factorial(numero_dado)
        print(f"El factorial de {numero_dado} es: {factorial}")
    except ValueError as ve:
        print(ve)