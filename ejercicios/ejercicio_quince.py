def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

cadena_ingresada = input("Ingrese una cadena de texto: ")

if es_palindromo(cadena_ingresada):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")