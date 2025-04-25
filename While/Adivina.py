# El programa elige un número secreto (por ahora lo pones tú, por ejemplo el 7)
# El usuario intenta adivinarlo. El bucle se repite hasta que adivine

secret = 7

print("Adivina el numero secreto que pienso")
num = int(input("Elije tu opcion: "))

while num != secret:
    print("No estoy pensando en ese numero")
    num = int(input("Vuelvelo a intentar: "))

