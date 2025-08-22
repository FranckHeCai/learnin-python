import re
# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
  print(f"He encontrado el patrón en el texto en la posición {found_ia.start()} y termina en la posición {found_ia.end()}")
else:
  print("No he encontrado el patrón en el texto")

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"
found_midu = re.finditer(pattern, text)
if found_midu:
  for midu in found_midu:
    print(f"midu encontrado en la posicion {midu.start()} y acaba en la posicion: {midu.end()}")
  print(f"Hay en total de {len(re.findall(pattern, text))} ocurrencias de la palabra 'midu'")

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
patten = "python"
matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)