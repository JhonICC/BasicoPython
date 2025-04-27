# Suma solo los números que estén en posición par (índices 0, 2, 4, etc.)

numbers = [10, 20, 30, 40, 50, 60]

suma = 0

for i in range (0, len(numbers), 2):
    suma += numbers[i]

print ("La suma de los numeros en posicion par es: ", suma)
