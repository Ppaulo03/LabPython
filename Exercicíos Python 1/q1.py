'''
1. Receba as informações de dois números e imprima a soma dos dois números
na tela.
'''

def get_num(nome):
    while True:
        i = input(str(nome) + ': ')
        i = i.replace(' ','').replace(',','.')
        if str(i).replace('-', '').replace('.', '').replace(',','').isdigit(): break
        print(i + ' não é um número. Tente novamente.')
            
    if '.' in i or ',' in i: return float(i)
    else: return int(i)


def soma():
    a = get_num('a')
    b = get_num('b')
    return a + b


if __name__ == '__main__':
    while True:
        print(soma())
        print('-'*10)