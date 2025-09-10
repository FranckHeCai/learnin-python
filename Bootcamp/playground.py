def comprobar_longitud(str):
    return len(str) >= 7

def comprobar_primero(str):
    return str[0].isupper()

def comprobar_ultimo(str):
    return str[len(str)-1].isnumeric()

password = input()

if not comprobar_longitud(password):
    print("Incorrecta. Debe comenzar tener al menos 7 caracteres")
elif not comprobar_primero(password):
    print("Incorrecta. Debe comenzar con una vocal mayúscula")
elif not comprobar_ultimo(password):
    print("Incorrecta. Debe acabar con un numero")
else:
    print(f"Correcta. La contraseña es: {password}")