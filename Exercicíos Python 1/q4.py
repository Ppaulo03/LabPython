
'''
4. Receba a informação de temperatura em Célsius, converta para Fahrenheit e
escreva na tela o resultado. (Fórmula: F = C * 1.8 + 32)
'''
def celsius_to_fahrenheit():
    temp_C = input("Informe a temperatura: ")
    temp_F = (float(temp_C)*1.8)+32
    print(temp_F)

if __name__ == '__main__':
    celsius_to_fahrenheit()
 
