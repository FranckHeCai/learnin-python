import os
os.system("clear")

print("Simple conditional statements")
edad = 99
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("Conditional statements with elif")

nota = 10
if nota >= 9:
    if nota == 10:
        print("Matricula de Honor")
    else:
        print("Excelente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspendido")

print("Multiple conditions with logical operators")
tiene_carnet = True

if edad >= 18 and edad <=80 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")

if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("Sobarna al policia")

fin_de_semana = False

if not fin_de_semana:
    print("A trabajar")
else:
    print("A descansar")