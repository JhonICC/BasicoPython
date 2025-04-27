# A partir de dos listas, crea una nueva lista en orden

list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = []

for a, b in zip(list1, list2): #Usamos zip para recorrer las 2 listas a la vez
    new_list.append(a)
    new_list.append(b)

print("Nueva lista:", new_list)
