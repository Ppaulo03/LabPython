ano = int(input("Escreva um ano: "))
bissexto = True
if ano % 4 != 0: bissexto = False
elif ano % 100 == 0 and ano % 400 != 0: bissexto = False

if bissexto: print('O ano é bissexto')
else: print('O ano não é bissexto')