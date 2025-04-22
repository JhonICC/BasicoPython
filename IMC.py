# Pide el peso (kg) y la altura (m) del usuario y calcula el IMC con la fórmula:
# imc = peso / (altura ** 2)

height = float(input("Dame tu altura: "))
weight = int(input("Dame tu peso: "))
imc = weight/(height**2) #Forma de hacer el cuadrado de un numero

if imc < 18.5:
    print("Bajo peso")
elif imc > 18.5 and imc < 24.9:
    print("Peso normal")
elif imc > 25 and imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")
