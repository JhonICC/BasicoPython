# Muestra las palabras que empiezan por vocal

words = ["elefante", "tigre", "oso", "iguana", "gato"]

for word in words:
    if word[0] in "aeiou": # Forma de que tome en cuenta solo la primera letra
        print(word)

