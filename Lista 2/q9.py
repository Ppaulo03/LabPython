print('Equação do segundo grau -> ax²+bx+c')
a = float(input('a: '))
if a == 0:
    print('Equação não é de 2° grau, a deve ser diferente de 0')
else:
    b = float(input('b: '))
    c = float(input('c: '))

    delta = b**2 - 4*a*c
    if delta < 0: print('Equação não possui raizes reais!!')

    elif delta == 0:
        print('Equação possuí apenas 1 raiz real: ')
        raiz = (-b + delta**0.5)/(2*a)
        print(f'Raiz: {raiz}')
    
    else:
        print('Equação possuí 2 raizes reais: ')
        raiz1 = (-b + delta**0.5)/(2*a)
        raiz2 = (-b - delta**0.5)/(2*a)
        print(f'1° Raiz: {raiz1}')
        print(f'2° Raiz: {raiz2}')
