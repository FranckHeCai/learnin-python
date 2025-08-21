#Equilibrio 4 fantastico
import os
os.system("clear")
def balance(text):
  """ Indica la cantidad de letra r y j hay en la cadena. Si la cantidad es igual devuelve true"""
  richard = text.lower().count("r")
  james = text.lower().count("j")

  #return True if james == richard else False
  return james == richard

print(balance("hello"))