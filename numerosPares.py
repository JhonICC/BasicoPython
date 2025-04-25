# Crea una lista con los números del 1 al 20
# Usa un bucle para mostrar solo los números pares

numbers = list(range(1,21)) # Forma de hacer un rango para una lista

for number in numbers:
    if number % 2 == 0:
        print(number)

