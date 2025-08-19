def saludar(nombre):
  return f"Hola soy {nombre}"

def edad(edad, nombre, func):
  print(f"{func(nombre)} y tengo {edad} de edad")

edad(25, "Zuko", saludar)
