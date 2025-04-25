# Pide números y los vas sumando
# El programa termina cuando el usuario introduce un 0

result = 0

print("El numero inicial es: ", result)

sum = int(input("Introduce que numero quieres sumar: "))

while sum != 0:
    print("El resultado es:", result + sum)
    result = result + sum
    sum = int(input("Que otro numero quieres sumar: "))

print("El resultado final es:", result)
