# Pide al usuario una palabra y muestra si es un palíndromo (se lee igual al revés)

word = input("Introduce una palabra: ")

if word == word[::-1]: # Forma se que lea la palabra o la frase al reves
    print("Es un polindromo")
else:
    print("No es un polindromo")

