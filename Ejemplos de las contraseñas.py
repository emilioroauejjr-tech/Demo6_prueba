import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Longitud = int(input("Ingrese la longitud de la contraseña: "))
Resultado = ""
for i in range(Longitud):
    Resultado += random.choice(caracteres)



print("Aquí tu contraseña generada: " + Resultado)
