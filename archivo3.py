#leer los nombres, apl

nombres = input("dime tus nombres: ")
apellidos = input("dime tus apellidos: ")
edad = input("dime tu edad: ")
carrera = input("dime tu carrera: ")

datos = f"nombres: {nombres.title()}\napellidos: {apellidos.title()}\nedad: {edad}\ncarrera: {carrera.title()}"

with open("estudiantes.txt", "w", encoding="utf-8") as archivo:
    archivo.write(datos)

print("archivo creado satisfactoriamente")