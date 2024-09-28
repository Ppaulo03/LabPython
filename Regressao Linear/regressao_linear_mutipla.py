from operacoes_matriciais import *


def minimos_mutiplos_quadrados(xt:list[list[float]], y:list[float]) -> list[float]:
    '''Retorna os coeficientes da regressão linear pelo método dos mínimos múltiplos quadrados'''
    n = len(y)

    for linha in xt:
        if len(linha) != n: raise ValueError('Tamanhos da matriz de entrada inválida')

    xt = [[1 for _ in range(n)]] + xt
    x = m_transpor(xt)
    y = m_transpor([y])
    b = m_multiplicar(m_multiplicar(m_inverter(m_multiplicar(xt, x)), xt), y)
    return m_transpor(b)[0]

def indices_de_erro(x, y, b):
    '''Retorna os índices de erro da regressão linear'''
    n = len(y)
    y_media = sum(y)/n
    
    sqr, sqt, sqe = 0, 0, 0
    y_chas  = []
    for i in range(len(y)):
        y_chapeu = b[0] + sum([b[j+1]*x[j][i] for j in range(len(b)-1)])
        y_chas.append(y_chapeu)

        sqr += (y[i] - y_chapeu)**2
        sqt += (y[i] - y_media)**2
        sqe += (y_chapeu - y_media)**2
    
    s = (sqr/(n-len(b)))**0.5

    r_2 = sqe/sqt
    r_2_ajustado = 1 - (((1 - r_2)*(n-1))/(n-len(b)))

    return s, r_2, r_2_ajustado


if __name__ == '__main__':
    y  = [  122,  114,    86, 134,  146,  107,    68,  117,  71,    98]
    x1 = [  139,  126,    90, 144,  163,  136,    61,   62,  41,   120]
    x2 = [0.115, 0.12, 0.105, 0.09, 0.1, 0.12, 0.105, 0.08, 0.1, 0.115]
    
    b = minimos_mutiplos_quadrados([x1, x2], y)
    s, r_2, r_2_ajustado = indices_de_erro([x1, x2], y, b)
    print(b)
    print('Erro padrão dos resíduos:', s)
    print('                      R²:', r_2)
    print('             R² ajustado:', r_2_ajustado)
    