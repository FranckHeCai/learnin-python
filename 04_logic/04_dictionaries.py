###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###
import os
os.system("clear")

a = {
  "name": "piccolo",
  "rich": "True"
}
b = {
  "name": "Zuko"
}

a.update(b)
print(a)