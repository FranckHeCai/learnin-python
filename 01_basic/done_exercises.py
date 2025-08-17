###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
nombre = "Zuko"
ciudad = "Ciudad del Fuego"
print(f"Nombre : {nombre}  \nCiudad: {ciudad}")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"a: {type(a)}")
print(f"b: {type(b)}")
print(f"c: {type(c)}")
print(f"d: {type(d)}")
print(f"e: {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
print(int("12345"), "number")
print(float("12345"), "float")
print(int(3.99), "3.99 float -> int")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
edad = 25
altura = 1.75
print(f"Hola, me llamo {nombre}, mido {altura} metros y tengo {edad} de edad.")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")
### Completa aquí
pi = 3.14159
print(f"PI: {pi}")
print(f"PI redondeado: {round(pi)}")
resultado = round(pi)/pi
print(f"Resultado de la division : {resultado}")