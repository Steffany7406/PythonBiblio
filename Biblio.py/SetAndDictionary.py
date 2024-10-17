
"""
Os Sets são uma lista desordenada, imutavel e não aceita valores duplicados.
Já os Dicionarios são coleções de chave e valor
dicionarios não são ordenados(não tem index), não aceitam duplicados, 
mas é mutavel(você pode adicionar mais valores depois de criado)
tanto o set quanto o dicionario tem a propriedade len() para retornar o numero de itens na coleção, 
assim como vimos na list e no tuple
"""

# Exemplo de uso de set
frutas = {'maçã', 'laranja', 'abacaxi'} #Set de strings
#Como é uma lista desordenada não temos indice
#No caso de uma repetição de valores, ele ignora o segundo valor
#Sempre que executa ele impugna uma ordem diferente dos itens
frutas.add("Pera") #Podemos adicionar frutas
frutas.pop() #E remover o último valor
frutas.remove("maçã") #Remover frutas
#print(frutas) 

#Set numerico
set = {0, 3, 50, -74}

#Set booleano
set = {True, False, False, True}

#E podemos criar um set que exiba os três. 
set = {"maçã", 3, True}

#--------------------------------------------------------------

#Exemplo de uso de dicionario
#Os dicionários também são mutaveis, não tem indice e não são ordenados.

meses = {
    "Janeiro": 31, #A chave é a primeira coluna antes dos dois pontos
    "Fevereiro": 28, #Pode ser qualquer tipo de dado
    "Março": 31, #Ele também ignora valor duplicado
    "Abril": 30, 
    "Maio": 31,
    "Junho": 30,
    "Julho": 31,
    "Agosto": 31,
    "Setembro": 30,
    "Outubro": 31,
    "Novembro": 30,
    "Dezembro": 31
}

#print(meses["Agosto"])  #Acessar um valor pelo seu nome e diz o total de dias que cada mês

#A diferença de chamar ele com [] de com get é que se for chamado um valor invalido ele vai dar um erro
# Já com Get  ele vai dar um valor default(NaN)

#print(meses.get('Agosto', 'Padrão')) 
#O segundo parametro é o Padrão, um pedido de valor que você quer que ele traga caso o primeiro seja invalido. 
print(meses.get("Abc", 'Janeiro')) #Se o valor não existir ele vai trazer o valor default que é 'Janeiro'
