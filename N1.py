import os
import sys
from enum import Enum


#Conversors

def binary_to_decimal(binary:str) -> str:
    decimal = 0
    for pos, c in enumerate(binary[::-1]):
        if c == '1': decimal += 2**pos
    return decimal, 'decimal'


def decimal_to_binary(decimal:str) -> str:
    decimal = int(decimal)
    binary = ''
    
    remainder = decimal%2
    decimal //= 2
    binary += str(remainder)

    while decimal > 0:
        remainder = decimal%2
        decimal //= 2
        binary += str(remainder)

    return binary[::-1], 'binário'

hexa_to_binary_dict = { '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
                        '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111',}

def hexadecimal_to_binary(hexadecimal:str) -> str:
    binary = ''
    hexadecimal = hexadecimal.upper()
    for c in hexadecimal:
        binary += hexa_to_binary_dict[c]

    return binary, 'binário'


binary_to_hexa_dict = { '0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7', 
                        '1000':'8', '1001':'9', '1010':'A', '1011':'B', '1100':'C', '1101':'D', '1110':'E', '1111':'F'}

def binary_to_hexadecimal(binary:str) -> str:
    hexadecimal = ''
    if len(binary)%4 != 0:
        binary = '0'*(4-len(binary)%4) + binary
    
    for i in range(0, len(binary), 4):
        c = binary[i:i+4]
        hexadecimal += binary_to_hexa_dict[c]
       
    return hexadecimal, 'hexadecimal'


def remove_sign(entrada:str) -> list[str, bool]:
    entrada = entrada.replace(' ', '')
    negativo = False
    if entrada[0] == '+' or entrada[0] == '-':
        if entrada[0] == '-': negativo = True
        if len(entrada) > 1: entrada = entrada[1:]
        else: entrada = ''
    return [entrada, negativo]

#------------------------------------------------------------------------------------------------------------------------------------

#Validators

def validator_decimal(entrada:str) -> bool:
    if len(entrada) == 0: return False
    return entrada.isdigit()


def validator_binary(entrada:str) -> bool:
    if len(entrada) == 0: return False
    binary_opt = ['0', '1']
    for c in entrada:
        if c not in binary_opt: return False
    return True


def validator_hexadecimal(entrada:str) -> bool:
    if len(entrada) == 0: return False
    entrada = entrada.upper()
    hexa_opt = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    for c in entrada:
        if c not in hexa_opt: return False
    return True



class InvalidInput(Exception): pass
#------------------------------------------------------------------------------------------------------------------------------------


class color(Enum):
    WHITE = 0
    RED = 1
    PURPLE = 2
    CYAN = 3
    DARKCYAN = 4
    BLUE = 5
    GREEN = 6
    YELLOW = 7

def print_especial(msg:str, color:color = color.WHITE, bold:bool=False, underline:bool=False) -> None:
    spec = ''
    
    match color:
        case color.RED: spec = '\033[91m'
        case color.PURPLE: spec = '\033[95m'
        case color.CYAN: spec = '\033[96m'
        case color.DARKCYAN: spec = '\033[36m'
        case color.BLUE: spec = '\033[94m'
        case color.GREEN: spec = '\033[92m'
        case color.YELLOW: spec = '\033[93m'
    
    if bold: spec += '\033[1m'
    if underline: spec += '\033[4m'
    
    msg = spec + msg
    if len(spec) > 0: msg += '\033[0m'
    print(msg, end='')
    

comand_dict={
    '1':'1. Binário para Decimal',
    '2':'2. Binário para Hexadecimal',
    '3':'3. Decimal para Binário',
    '4':'4. Decimal para Hexadecimal',
    '5':'5. Hexadecimal para Binário',
    '6':'6. Hexadecimal para Decimal',
    '7':'7. Sair'
} 

bases_msg = [
    ('Digite um número em binário (0 e 1): ', validator_binary),
    ('Digite um número na base decimal (digítos de 0 a 9): ', validator_decimal),
    ('Digite um número em hexadecimal (digítos de 0 a F): ', validator_hexadecimal),
    ('', None)
]


def show_comands() -> str:
    print('Escolha o tipo de conversão\n')
    for value in comand_dict.values():
        print(value)
    print('\n')
    command = ''
    while len(command) == 0:
        sys.stdout.write("\033[F")
        print('Comando: ', end = '')
        command = input().strip()
       
    os.system('cls')
    return command


def get_entrada(validator, msg):
    if validator is None: return None, None
    entrada = ''
    print('')
    while len(entrada) == 0:
        sys.stdout.write("\033[F")
        print(msg, end = '')
        entrada = input().strip()
    entrada, negativo = remove_sign(entrada)
    if not validator(entrada): raise InvalidInput()
    return entrada, negativo


def show_result(valor:str, negativo:bool, tipo:str)->None:
    if negativo: valor = "-" + valor
    print_especial(f'Valor em {tipo}: ', color=color.GREEN)
    print_especial(f'{valor}\n', color=color.GREEN, bold=True)
    print('Clique enter para voltar ao menu ', end='')
    input()
    os.system('cls')


while True:
    command = show_comands()
    if command in comand_dict.keys():
        print(comand_dict[command])
       
        try:
            idx = (int(command)-1)//2
            entrada, negativo = get_entrada(bases_msg[idx][1], bases_msg[idx][0])
        except InvalidInput: 
            print_especial('Entrada inválida para base escolhida!\n', color.RED, bold=True)
            continue
    else: 
        print_especial('Comando inválido!!\n', color.RED, bold=True)
        continue

    match command:
        case '1' : result, tipo = binary_to_decimal(entrada)
        
        case '2' : result, tipo = binary_to_hexadecimal(entrada)
        
        case '3' : result, tipo = decimal_to_binary(entrada)
        
        case '4' :
            binary, _ = decimal_to_binary(entrada)
            result, tipo = str(binary_to_hexadecimal(str(binary)))
        
        case '5' : result, tipo = hexadecimal_to_binary(entrada)
        
        case '6' : 
            binary, _ = hexadecimal_to_binary(entrada)
            result, tipo = binary_to_decimal(str(binary))
        
        case '7' : break
    show_result(str(result), negativo, tipo)

os.system('cls')