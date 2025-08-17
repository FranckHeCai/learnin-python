###
# EJERCICIOS
###
import os
os.system("clear")
# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("Ejercicio 1: Determinar el mayor de dos números")
num1, num2 = input("Introduce el numero 1: "), input("Introduce el numero 2: ")
print(f"{num1} es mayor que {num2}" if num1 > num2 else f"{num2} es mayor que {num1}")
print("----------")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("Ejercicio 2: Calculadora simple")
num1, num2 = int(input("Introduce el numero 1: ")), int(input("Introduce el numero 2: "))
operacion = input("Introduce la operacion (+, -, *, /): ")
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero"
print(f"El resultado es: {resultado}")
print("----------")
# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("Ejercicio 3: Año bisiesto")
ano = int(input("Introduce un año: "))
if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
  print("Año bisiesto")
else:
  print("Año no bisiesto")

print("----------")
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
print("Ejercicio 4: Categorizar edades")
edad = int(input("Introduce tu edad: "))
if edad <= 2:
    print("Eres un bebé")
elif edad <= 12:
    print("Eres un niño")
elif edad <= 17:
    print("Eres un adolescente")
elif edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
print("----------")