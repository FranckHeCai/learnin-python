import re
import os
os.system("clear")

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34

text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: print(f"Encontré el número de teléfono {found.group()}")

# EJERCICIO
# Valida que un correo sea de gmail
text = "miduga@hotmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)

if valid: print("El correo es gmail válido")
else: print("El correo no es válido")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\.txt$"
matches = re.findall(pattern, files)
print(matches)