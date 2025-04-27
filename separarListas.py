# Pide al usuario 10 numeros y guardalos en dos listas
# Primera lista de pares
# Segunda lista de impares

par = []
impar = []

for i in range(10):
    number = int(input("Introduce un numero: "))

    if number % 2 == 0: # Verificar si el número es par
        par.append(number)
    else:
        impar.append(number)

print("Lista de números pares:", par)
print("Lista de números impares:", impar)