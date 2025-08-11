print("Simple conditional statements")
edad = 18
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
