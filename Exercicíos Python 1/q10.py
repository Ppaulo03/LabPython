'''
10. Receba as informações de peso e altura de uma pessoa e escreva na tela o IMC dela.
(Fórmula: IMC = peso / altura²)
'''

def imc():
    peso = float(input('Digite o peso da pessoa: '))
    altura = float(input('Digite a altura da pessoa: '))
    
    imc = peso / altura**2
    print(f'O IMC da pessoa é {imc}')

if __name__ == '__main__':
    imc()