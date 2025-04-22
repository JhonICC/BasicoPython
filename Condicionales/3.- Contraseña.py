# Pide una contraseña al usuario. Si es correcta, muestra "Acceso permitido".
# Si no, "Acceso denegado".

contraseña = "Contraseña12"
password = input("Introduce contraseña: ")

if password == contraseña:
    print("Acceso permitido")
else:
    print("Acceso denegado")
