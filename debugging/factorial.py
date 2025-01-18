#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) > 1:
    try:
        n = int(sys.argv[1])
        if n < 0:
            print("El factorial no está definido para números negativos.")
        else:
            f = factorial(n)
            print(f"El factorial de {n} es {f}.")
    except ValueError:
        print("Por favor, introduce un número entero válido.")
else:
    print("Por favor, proporciona un número como argumento.")
