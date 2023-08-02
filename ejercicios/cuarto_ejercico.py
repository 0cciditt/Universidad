def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

numero_dado = int(input("Ingrese un número: "))


resultado = es_par_o_impar(numero_dado)
print(resultado)
