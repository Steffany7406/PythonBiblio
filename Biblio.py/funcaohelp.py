help(print) #Mostra a documentação do print.
""" 
A função help ajuda a entender melhor uma documentação que você não saiba
que existe. Por exemplo, se você quiser saber como funciona a função print, basta usar
help(print) e ele irá mostrar a documentação da função print.
"""

def calcular_imposto(faturamento, taxa):
    """ 
    faturamento(float): o faturamento da empresa que vamos calcular o imposto
    taxa(float): a taxa percentual de imposto sobre o faturamento (ex: 0,2)

    return imposto, faturamento_liquido
    imposto(float): valor total do imposto calculado sobre o faturamento
    faturamento_liquido (float):quanto sobrou do faturamento depois de descontado o imposto
    """

    imposto = faturamento * taxa
    return imposto, faturamento - imposto

help(calcular_imposto)    