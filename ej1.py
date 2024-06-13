
# Datos proporcionados
datos = [(3, 5), (7, 8)]

# Ejemplo de salida esperada
# 3 * 5 = 15
# 7 * 8 = 56

def multiplicar(a,b):
    resultado = 0
    for i in range(b):
        resultado = resultado + a
    return resultado

def multiplicar2(a,b):
    resultado = 0
    i = 0
    while(i<b):
        resultado = resultado + a
        i = i + 1
    return resultado

for i in datos:
    print(multiplicar(i[0], i[1]))
