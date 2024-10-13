#Funções conjunto de código de lógica de programação.
#O principal uso da criação de funções é sua reutilização
"""
def big_mac():
    print('Sanduiche big mac')


print('inicio')
big_mac()
big_mac()
big_mac()
big_mac()
big_mac()
big_mac()
big_mac()
big_mac()
print('fim')
"""

#Funções com parâmetros
def fazer_big_mac(nome):
    print(f'Sanduiche Big Mac para {nome}')

def fazer_batata(tamanho):
    print(f'Batata {tamanho}')

def servir_refrigerante(tipo, tamanho):
    print(f'{tipo} {tamanho}')

#fazer_big_mac('Thais')
#fazer_batata('Grande')
#servir_refrigerante('Coca-Cola', 'Grande')

def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    servir_refrigerante(tipo_refri,tamanho_refri)

#fazer_combo_big_mac('Steffany', 'Grande', 'Coca', 'Grande') 

def soma_num(num1, num2):
    return num1 + num2
resultado = soma_num(25, 46) 
#print(resultado) = Output: 71

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num =  lista_num[0]
    return maior_num
    #return max(lista_num)
resultado = maior_num([9, 49, 55, 87, 36, 54, 12])
#print(resultado) = Output: 87
