# Encuentra el numero mas grande y mas pequeño de la lista

numbers = [7, 3, 9, 2, 8, 5]

# Asumimos que el primer número es el mayor y el menor
mayor = numbers[0]
menor = numbers[0]

for number in numbers: # Lee la lista
    if number > mayor: # Lee si el numero es mayor que el numero asignado al mayor
        mayor = number # De ser asi, se guarda, y asi se repite el bucle
    if number < menor:
        menor = number

print("El número más grande es:", mayor)
print("El número más pequeño es:", menor)
