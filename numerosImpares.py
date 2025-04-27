# Elimina los impares y deja solo los pares.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_pares = []

for i in numbers:
    if i % 2 == 0:
        numbers_pares.append(i)

print(numbers_pares)
