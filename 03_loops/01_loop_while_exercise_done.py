###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

contador = 10
while contador > 0:
    print(contador)
    contador -= 1
# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
contador = 0
suma = 0
while contador <=20:
    contador += 1
    if contador % 2 == 0:
        suma += contador
print(f"La suma de los números pares entre 1 y 20 es: {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
try:
    numero = int(input("Introduce un número entero positivo: "))
    factorial = 1
    while numero > 0:
        factorial *= numero
        numero -= 1
    print(f"El factorial es: {factorial}")
        
except:
    print("Por favor, introduce un número entero válido.")
# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
contraseña = input("Introduce una contraseña (mínimo 8 caracteres): ")
while len(contraseña) < 8:
    contraseña = input("Contraseña inválida. Por favor, introduce una contraseña de al menos 8 caracteres: ")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
contador = 1
while contador <= 10:
    print(f"{numero} x {contador} = {contador * numero}")
    contador += 1
# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
numero = int(input("Introduce un numero entero positivo N:"))
contador = numero
while contador >= 1:
    prime = True
    i = 2
    while i < contador:
        if contador % i == 0:
            prime = False
            break
        i += 1
    print(f"{contador} es primo") if prime else print(f"{contador} no es primo")
    contador -= 1