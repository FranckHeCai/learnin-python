import os
os.system('clear')
# Bucles while

print("Bucle while")
# Contador simple
contador = 0
while contador < 5:
    print("Contador:", contador + 1)
    contador += 1
print("Fin del bucle")

contador = 0
while True:
    print(contador + 1)
    contador += 1
    if contador >= 5:
        break


# Bucle con continue, lo que hace es saltar a la siguiente iteración
print("Bucle con continue")
contador = 0
while contador < 5:
    contador += 1
    if contador % 2 == 0:
        print(f'{contador} es par')
        continue
    print(f'{contador} es impar')

# Bucle con else, se ejecuta cuando el bucle termina sin interrupciones
print("Bucle con else")
contador = 0
while contador < 5:
    contador += 1
    print("Contador:", contador)
else:
    print("Bucle terminado sin interrupciones")

# Pedir numero positivo al usuario si no lo es, volver a pedirlo

# while True:
#     numero = input('Introduce un numero positivo: ')
#     if int(numero) > 0:
#         print(f'El numero {numero} es positivo')
#         break
numero = input('Introduce un numero positivo: ')
while int(numero) <= 0:
    numero = input('El numero no es positivo, vuelve a intentarlo: ')
    if int(numero) > 0:
        print(f'El numero {numero} es positivo')
        break  
  
# Pedir el numero positivo con try except
numero = input('Introduce un numero positivo: ')
while int(numero) <= 0:
    try:
      numero = input('El numero no es positivo, vuelve a intentarlo: ')
      if int(numero) > 0:
        print(f'El numero {numero} es positivo')
        break 
    except:
        numero = input('El valor introducido no es un numero, vuelve a intentarlo: ') 
