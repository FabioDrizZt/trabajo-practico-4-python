
# Datos proporcionados
datos = [20, 14]

# Ejemplo de salida esperada
# Para 20: [20, 18, 16, ..., 2]
# Para 14: [14, 12, 10, ..., 2]

def paresOrdenDescendente(a):
    lista = []
    for i in range(20, 1, -2):
        lista.append(i)
    return lista

for i in datos:
    print(paresOrdenDescendente(i))
