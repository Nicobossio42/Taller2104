numeros = [45, 49, 0, -18, 3, 0, -3, 58, 28, -19]
positivos = []

for num in numeros:
    if num > 0:
        positivos.append(num)

print('Vector original')
print(numeros)
print()
print('Vector con solo números positivos')
print(positivos)

#La salida de este codigo, saca primeramente los numeros completos
#despues se les pone los mismos numeros pero solo con positivos.