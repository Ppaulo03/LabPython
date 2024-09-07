'''
8. Receba as informações de 4 notas e escreva na tela o resultado da média.
'''

def media():
    notas = []
    for i in range(4):
        nota = float(input(f'Digite a nota {i+1}: '))
        notas.append(nota)
    
    media = sum(notas)/len(notas)
    print(f'A média das notas é {media}')

if __name__ == '__main__':
    media()