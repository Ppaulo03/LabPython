def soma_tudo(a, b, c, d, e): #1
    return a + b + c + d + e 

def dolar_para_real(dolar): #2 #Dólar a R$5,48, dia 03/10/2024 às 20:12
    return dolar * 5.48

def fibonacci(n): #3 
    if n <= 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n - 1) + fibonacci(n - 2)

def find_letter(text, letter): #4
    text = text.lower()
    letter = letter.lower()
    i = text.find(letter)
    return i

def count_vogals(text): #5
    text = text.lower()
    vogais = ['a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'ü']
    cont = 0
    for c in text:
        if c in vogais: cont += 1
    
    return cont

def cont_words(text): #6
    text = text.replace('  ', ' ').strip().split(' ')
    return len(text)

def is_palindromo(text): #7
    text = text.lower()
    return text == text[::-1]


import random
def random_dice(n): #7
    faces = [0 for i in range(6)]
    for i in range(n):
        idx = random.randint(0, 5)
        faces[idx] += 1
    return faces

if __name__ == '__main__':
    soma = soma_tudo(1,2,3,4,5)
    print(f'#1 - soma de 1, 2, 3, 4, 5: {soma}', end='\n\n')

    real = dolar_para_real(100)
    print(f'#2 Conversão de $100 para reais: R${real}', end='\n\n')

    fib_20 = fibonacci(20)
    print(f'#3 20° Termo de Fibonnaci: {fib_20}', end='\n\n')

    pos = find_letter('barco', 'a')
    print(f'#4 Posição da letra "a" em "barco": {pos+1}ª', end='\n\n')

    num_vog = count_vogals('arara')
    print(f'#5 Quantidade de vogais em "arara"', end='\n\n')

    num_words = cont_words('Hello World')
    print(f'#6 Número de palavras em "Hello World"', end='\n\n')

    palindromo = is_palindromo('arara')
    print(f'#7 "Arara" é palindromo? {palindromo}', end='\n\n')

    faces = random_dice(100)

    print('Quantidade de vezes que cada face de um dado de 6 lados caiu em 100 jogadas:')
    for i in range(6):
        print(f'Face {i+1}: {faces[i]} vezes')
