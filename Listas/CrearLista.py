# Crear lista desde input y recorrerla

fruit = []

for i in range(3): # Hace que se repita 3 veces
    fruta = input("Introduce una fruta: ")
    fruit.append(fruta)

print("Has introducido estas frutas:")
for fruta in fruit:
    print(fruta)
