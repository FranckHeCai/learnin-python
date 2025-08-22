##
# 01 - Expresiones regulares
# 

""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

# 1. Importar el módulo de expresiones regulares "re"
import re
# 2. Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"
# 3. El texto donde queremos buscar
text = "Hola mundo"
# 4. Usar la función de búsqueda de "re"
result = re.search(pattern, text)

if result:
  print("He encontrado el patrón en el texto")
else:
  print("No he encontrado el patrón en el texto")

# .group() devuelve la cadena que coincide con el pattern
print(result.group())

# .start() devolver la posición inicial de la coincidencia
print(result.start())

# .end() devolver la posición final de la coincidencia
print(result.end())

# -----------------------

### Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)

print(len(matches))
print(matches)
# -------------------------

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
  print(match.group(), match.start(), match.end())

### Modificadores

# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento

# re.IGNORECASE: Ignora las mayúsculas y minúsculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

if found: print(found)

### Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto

text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "hola"
replacement = "Adiós"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(new_text)



