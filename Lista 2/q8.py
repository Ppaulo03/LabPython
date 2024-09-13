valor_hora = float(input('Valor hora: '))
qtd_horas = int(input('Horas trabalhadas: '))

bruto = valor_hora * qtd_horas
if bruto < 1500: liquido = bruto
elif bruto < 1800: liquido = bruto*0.95
elif bruto < 2500: liquido = bruto*0.9
else: liquido = bruto*0.8
print(f'Sálario líquido: {liquido}')
