'''
2. Receba as informações de altura e largura de um retângulo e devolva a área
desse retângulo. (Fórmula: Area=L*A)
'''

def calcula_area_retangulo():
    l = input("Informe a largura: ")
    a = input("Informe a altura: ")
    area = float(l)*float(a)
    print("Área = " + str(area))

if __name__ == '__main__':
    calcula_area_retangulo()