'''
5. Receba a informação de temperatura em Fahrenheit, converta para Célsius e
escreva na tela o resultado. (Fórmula: C = (F − 32) * 5 / 9)
'''
def fahrenheit_to_celsius():
    temp_F = input("Informe a temperatura: ")
    temp_C = (float(temp_F)-32)*(5.0/9.0)
    print(temp_C)

if __name__ == '__main__':
    fahrenheit_to_celsius()
