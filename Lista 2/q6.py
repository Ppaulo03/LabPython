a = float(input("Escreva o primeiro lado: "))
b = float(input("Escreva o segundo lado: "))
c = float(input("Escreva o terceiro lado: "))
lados = [a, b, c]
maior_lado = max(lados)
lados.remove(maior_lado)
if lados[0] + lados[1] <= maior_lado: print('Não é um triângulo')
else:
    if a == b == c: print('Triângulo equilátero')
    elif a == b or a==c or b==c: print('Triângulo isósceles:')
    else: print('Triângulo Escaleno')