# Crea una lista vacía.
# Usa un bucle para llenar esa lista con los cuadrados de los números del 1 al 10

square = [] # Lista vacia

for numero in range (1,11):
    resultado = numero * numero # Guardamos el resultado de los cuadrados
    square.append(resultado)

print(square)
