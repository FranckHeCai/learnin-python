#range() crea una lista de números 
import os
os.system('clear')
nums = range(10) # NO CREA UNA LISTA, SINO UN OBJETO RANGE
for num in nums:
  print(num)

for num in range(0,10,2): # inicio, fin, paso
  print(num)

for num in range(10, 0, -1): # cuenta regresiva
  print(num)

nums = range(10)
list_nums = list(nums) # convertir a lista
print(list_nums)

text = "Python"
lista_text = list(text) # convertir a lista
print(lista_text)

