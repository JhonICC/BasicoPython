# Contar cuántas veces aparece una letra en una palabra

palabra = input("Escribe una palabra: ")
letra = input("Qué letra quieres contar?: ")
contador = 0

for caracter in palabra:
    if caracter == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces.")

