# Haz un menú con opciones que se repita hasta que el usuario escriba 5 (Salir)

print("****Calculadora****")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
print("5.- Salir")

option = int(input("Elije que deseas hacer: "))

while option != 5:
    print ("Opcion no disponible")
    option = int(input("Elije otra opcion: "))

