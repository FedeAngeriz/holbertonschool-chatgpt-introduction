#!/usr/bin/python3

#factorial: Calcula el numero factorial de un numero entero
#n: Numero entero a calcular
#Return: Devuelve el factorial del numero ingresado

import sys

def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
