'''
9. Receba as informações do salário bruto e desconte IR, INSS e sindicato, e devolva o
salário líquido. Valores de referência (IR 12%, INSS 8%, Sindicato 5%)
'''

def salario_liquido():
    salario_bruto = float(input('Digite o salário bruto: '))
    ir = salario_bruto * 0.12
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - ir - inss - sindicato
    print(f'Salário líquido: {salario_liquido}')

if __name__ == '__main__':
    salario_liquido()