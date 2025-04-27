# Crea una nueva lista sin duplicados, usando un bucle

numbers = [3, 5, 3, 7, 5, 9, 3]
no_repetidos = [] # Aqui añadiremos los numeros no repetidos

for number in numbers: # Recorre la lista
    if number not in no_repetidos: #Añade el numero en la nueva lista, solo si no esta
        no_repetidos.append(number)

print("Lista sin duplicados:", no_repetidos)

