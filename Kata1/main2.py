password = "contraseña"

password_del_usuario = input("introduzca la contraseña: ")
password_del_usuario = password_del_usuario.lower()

if password == password_del_usuario:
    print("El password es correcto")
else:
    print("EL password es incorrecto")
