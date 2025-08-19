# Bucle for para iterar sobre una lista
import os
os.system('clear')

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
  print(fruta)

#Iterar sobre una cadena de texto
cadena = "Python"
for letra in cadena:
  print(letra)

# enumerate() para obtener el índice y el valor
for index, fruta in enumerate(frutas):
  print(f"Índice: {index}, Fruta: {fruta}") 

# bucles anidados
letras = ["a", "b", "c"]
numeros = [1, 2, 3]
for letra in letras:
  for numero in numeros:
    print(f"{letra}{numero}")

#break y continue en bucles for
animales = ["perro", "gato", "pájaro", "pez", "panda", "elefante"]
for animal in animales:
  if animal == "panda":
    print(f"{animal} es un animal especial.")
    break

for index, animal in enumerate(animales):
  if animal == "panda":
    print(f"El {animal} se encuentra en el indice {index}")
    break

for animal in animales:
  if animal == "panda":
    continue
  print(animal)

animales_mayus = []
for animal in animales:
  animales_mayus.append(animal.upper())

pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]

