from operacoes_matriciais import *


def minimos_mutiplos_quadrados(xt, y):
    n = len(y)
    xt = [[1 for _ in range(n)]] + xt
    x = m_transpor(xt)
    y = m_transpor([y])
    b = m_multiplicar(m_multiplicar(m_inverter(m_multiplicar(xt, x)), xt), y)
    return m_transpor(b)[0]


if __name__ == '__main__':
    y  = [  122,  114,    86, 134,  146,  107,    68,  117,  71,    98]
    x1 = [  139,  126,    90, 144,  163,  136,    61,   62,  41,   120]
    x2 = [0.115, 0.12, 0.105, 0.09, 0.1, 0.12, 0.105, 0.08, 0.1, 0.115]
    
    b = minimos_mutiplos_quadrados([x1, x2], y)
    print(b)
    