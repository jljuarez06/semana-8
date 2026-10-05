#crea un programa que permita guardar n cantidad de notas en un archivo, leer las notas, calcular promedio, la nota mas alta y la nota mas baja



cantidad = int(input("dime la cantidad de notas: "))
notas = []

for i in range(cantidad):
    nota = float(input(f"introduce la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / cantidad
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

lineas_notas = ""
contador = 1
for n in notas:
    lineas_notas += f"Nota {contador}: {n}\n"
    contador +=1
    
datos = f"""--- Reporte de Notas ---
{lineas_notas}
-------------------
cantidad de notas:{cantidad}
promedio: {promedio:2f}
nota mas alta: {nota_mas_alta}
nota mas baja: {nota_mas_baja}"""

with open("estudiantes_notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write(datos)

print("\n--- Archivo guardado con exito. contenido: ---")
with open("estudiantes_notas.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())