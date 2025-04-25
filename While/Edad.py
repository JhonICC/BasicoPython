# Pide al usuario una edad, pero solo acepta valores entre 0 y 120
# Sigue pidiendo hasta que dé un valor válido

age = int(input("Que edad tienes? "))

while age <= 0 or age >=120:
    print("Edad no valida")
    age = int(input("Vuelve a introducir la edad: "))

    print("Tienes", age, "años")

