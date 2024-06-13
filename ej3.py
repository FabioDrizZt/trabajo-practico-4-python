
# Salida esperada
# Impares: [1, 3, 5, ..., 999]
# Pares: [2, 4, 6, ..., 1000]

pares = []
impares = []

for i in range(1, 1000, 2):
    impares.append(i)

for i in range(2, 1001, 2):
    pares.append(i)

print(pares)
print(impares)