import os
os.system("clear")
# List Methods
lista1 = [1, 2, 3, 4, 5]
lista1.append(6)  # Añadir un elemento al final
print(lista1)

lista1 = ['a', 'c', 'd']
lista1.insert(1, 'b')  # Insertar un elemento en una posición específica
print(lista1)

lista1.extend(['e', 'f'])  # Añadir múltiples elementos al final
print(lista1)

lista1.remove('f')  # Eliminar un elemento específico, solo elimina la primera ocurrencia
print(lista1)

# lista1.append('h','i') 
# print(lista1)  # Esto causará un error porque append solo acepta un argumento

ultimo = lista1.pop()  # Eliminar el último elemento y devolverlo
primero = lista1.pop(0)  # Eliminar el primer elemento y devolverlo
print(ultimo)
print(primero)

del lista1[-1]  # Eliminar el primer elemento por índice
print(lista1)

lista1.clear()  # Limpiar la lista
print("Lista después de limpiar:", lista1)

lista1 = ['panda', 'koala', 'gato', 'perro', 'lobo']
del lista1[2:4]  # Eliminar un rango de elementos
print(lista1)

# Metodos utiles
print("Ordenar listas")
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Ordenar la lista en su lugar -- NO DEVUELVE LA LISTA LA MODIFICA DIRECTAMENTE
print(numbers)

print("Ordenar listas creando una nueva lista")
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)  # Crear una nueva lista ordenada SI QUE DEVUELVE LA LISTA
print(sorted_numbers)

print('Ordenar una lista de cadenas')
frutas = ['pera', 'manzana', 'limon', 'pera', 'manzana', 'limon']
sorted_frutas = sorted(frutas)  # Ordenar una lista de cadenas
print(sorted_frutas)

print('Ordenar una lista de cadenas')
frutas = ['pera', 'Manzana', 'limon', 'Pera', 'manzana', 'limon']
sorted_frutas = sorted(frutas)  # Ordena la lista de cadenas teniendo en cuenta mayúsculas y minúsculas
print(sorted_frutas)

print('Ordenar una lista de cadenas')
frutas = ['pera', 'manzana', 'limon', 'pera', 'manzana', 'limon']
frutas.sort(key=str.lower)  # Ordenar una lista de cadenas ignorando mayúsculas y minúsculas

# Otros metodos utiles
lista1 = ['panda', 'koala', 'gato', 'perro', 'lobo']
print(len(lista1))  # Longitud de la lista
print('panda' in lista1)  # Comprobar si un elemento está en la lista
print('panda' not in lista1)  # Comprobar si un elemento no está en la lista
print(lista1.index('gato'))  # Obtener el índice de un elemento
print(lista1.count('panda'))  # Contar cuántas veces aparece un elemento en la lista
print(lista1.count())  # Contar cuántos elementos hay en la lista

