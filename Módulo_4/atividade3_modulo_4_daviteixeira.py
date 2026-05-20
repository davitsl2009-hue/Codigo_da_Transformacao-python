'''

Percorra um conjunto de números e exiba pares e ímpares separadamente.
Dado um conjunto de números, use um loop para identificar quais são pares e quais são ímpares, exibindo cada categoria separadamente.

'''

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números ímpares:", impares)
