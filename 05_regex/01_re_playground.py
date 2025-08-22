# 01 Importar el modulo de expresiones regulares
import re

# 02 crear un patron, una cadena de texto queremos buscar
pattern = "Hola"

# 03 El texto dentro del cual queremos buscar el patron
text = "Hola Mundo"

# 04 Usar la funcion search() para buscar el patron
result = re.search(pattern, text)

# 05 Resultado de la busqueda
if result:
  print("Se ha encontrado el patron dentro del texto")
else:
  print("No se ha encontrado el patron")

# Devueve la cadena de texto que coincide
print(result.group()) 

# Indica donde empieza el patron
result.start()

# Indica donde acaba el patron
result.end()

# Indica el inicio y final del patron
result.span()



