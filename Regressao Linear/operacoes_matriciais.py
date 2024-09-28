def m_print(matriz:list[list[float]]) -> None:
    '''Imprime a matriz'''
    for linha in matriz: print(linha)


def m_transpor(matriz:list[list[float]]) -> list[list[float]]:
    '''Retorna a matriz transposta'''
    transposta = [[] for _ in range(len(matriz[0]))]
    for linha in matriz:
        for idx, item in enumerate(linha):
            transposta[idx].append(item)

    return transposta


def m_multiplicar(matriz_a:list[list[float]], matriz_b:list[list[float]]) -> list[list[float]]:
    '''Retorna a multiplicação de duas matrizes'''
    if len(matriz_a[0]) != len(matriz_b): raise ValueError('Matrizes incompatíveis para multiplicação')

    matriz_c = []
    for linha in matriz_a:
        linha_c = []

        for i in range(len(matriz_b[0])):
            c = 0
            for idx, l in enumerate(matriz_b):
                c += l[i]*linha[idx]
            linha_c.append(c)
        matriz_c.append(linha_c)
    
    return matriz_c


def m_inverter(matriz:list[list[float]]) -> list[list[float]]:
    '''Retorna a matriz inversa'''
    n = len(matriz)
    if n != len(matriz[0]): raise ValueError('Matriz não quadrada')

    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    matriz = [linha + linha_i for linha, linha_i in zip(matriz, I)]

    for i in range(n):
        if matriz[i][i] == 0: raise ValueError('Matriz singular')
        
        pivô = matriz[i][i]
        for j in range(2 * n):
            matriz[i][j] /= pivô
        
        for k in range(n):
            if k != i:
                fator = matriz[k][i]
                for j in range(2 * n):
                    matriz[k][j] -= fator * matriz[i][j]

    inversa = [linha[n:] for linha in matriz]
    return inversa