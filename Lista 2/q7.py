salario = float(input('Digite o sálario atual: '))
if salario < 1000: salario *= 1.2
elif salario < 1500: salario *= 1.15
elif salario < 2000: salario *= 1.1
else: salario *= 1.05
print(f'Novo sálario: {salario}')