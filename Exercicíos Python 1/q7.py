'''
7. Receba as informações a, b e c da formula de Bhaskara e devolva os valores x1 e x2 da
fórmula. Dica: para fazer a raiz quadrada, basta elevar o número por 0.5.
'''

def bhaskara():
    print('ax^2 + bx + c = 0')
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    
    delta = b**2 - 4*a*c
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    
    print(f'x1 = {x1}\nx2 = {x2}')

if __name__ == '__main__':
    bhaskara()
