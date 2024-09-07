'''
6. Receba a informação de dias, converta para segundos e escreva na tela para o
usuário.
'''

def dias_para_segundos():
    dias = int(input('Digite a quantidade de dias: '))
    segundos = dias * 24 * 60 * 60
    print(f'{dias} dias = {segundos} segundos.')

if __name__ == '__main__':
    dias_para_segundos()