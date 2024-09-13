a = float(input("Escreva um número: "))
b = float(input("Escreva outro número: "))
c = float(input("Escreva mais um número: "))
maior = a
menor = a

numeros = [b, c]
for i in numeros:
    if i > maior: maior = i
    elif i < meno: menor = i
print(f'Maior: {maior}')
print(f'Menor: {menor}')