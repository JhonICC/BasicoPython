# 1.- Presentación personal
# Guarda tu nombre, tu edad y tu ciudad en variables y muestra algo como:
# Hola, me llamo Carla, tengo 22 años y vivo en Barcelona.

name = "Tyler"
age = 25
city = "Barcelona"

print("Hola, me llamo", name, ", tengo", age, "años y vivo en", city)
# Queda "Tyler ,"
print("Hola, me llamo "+name+", tengo", age, "años y vivo en", city)
# Queda "Tyler,"
print(f"Hola, me llamo {name}, tengo {age} años y vivo en {city}")
# Otra forma de que me quede "Tyler," con la coma junto al nombre