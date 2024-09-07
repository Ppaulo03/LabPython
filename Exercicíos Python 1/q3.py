
'''
3. Receba a informação do raio de um círculo, calcule a área desse círculo e
escreva na tela o resultado. (Fórmula: A=PI*r²)
'''
def calcula_area_circulo():
    PI = 3.14
    r = input("Informe o raio: ")
    area = PI*(float(r)**2)
    print(area)

if __name__ == '__main__':
    calcula_area_circulo()
