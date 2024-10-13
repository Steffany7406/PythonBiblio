#String = Texto (Qualquer informção que você escreva dentro de aspas)

my_string = "Olá, mundo!"
#print(my_string) Saída: Olá, mundo!

#my_string = "Olá, mundo!" + " Eu estou aqui!" # Concatenar strings
#print(my_string) Saída: Olá, mundo! Eu estou aqui!

"""
FString  = Formatação de String (Usa chaves para formatar strings)
    Exemplo: nome = "João", idade = 30, cidade = "São Paulo"
print(f"{nome} tem {idade} anos e mora em {cidade}")
    Saída: João tem 30 anos e mora em São Paulo
"""

#Transformando string em maiusculo
print(my_string.upper()) # Saída: OLÁ, MUNDO!

#Transformando string em minusculo
print(my_string.lower()) # Saída: olá, mundo!

#Verificando se o texto é Upper ou lower = Ele devolve em valor booleano
print(my_string.isupper()) # Saída: False
print(my_string.islower()) # Saída: True

#Função strip = removendo espaços dentro do texto
print(my_string.strip()) # Saída: Olá, mundo!
#Para garantir que você consiga fazer comparações de dados recebidos pelo user com banco de dados
# é importante usar a função strip() para remover espaços desnecessários.

#Função Replace = substitui uma palavra por outra
print(my_string.replace("mundo", "mundo novo")) # Saída: Olá, mundo novo
#Ele também deixa maiusculo ou não e substitui qualquer palavra que você quiser.
#print(my_string.replace("m", "M", 1))

#Função len = verifica a quantidade de caracteres usando o indice
print(len(my_string)) # Saída: 11

#Função indice = verifica a posição de uma palavra dentro do texto
print(my_string[2]) # Saída: 
print(my_string.index("mundo")) # Saída: 7

#Pegando algumas letras
print(my_string[2:6]) #Saída: lá, m
#De trás pra frente
print(my_string[-1]) # Saída: !
print(my_string[-5:-1]) # Saída: undo

#Função index = passando um texto e retornando um indice
print(my_string.index("m")) # Saída: 5

#Verificando se uma palavra existe dentro do texto
print("mundo" in my_string) # Saída: True
print("mundo novo" in my_string) # Saída: False

#Fazendo um texto com multiplas linhas
x =  """Olá, mundo!
Eu sou um texto com multiplas linhas
e vou ser impresso aqui!"""
print(x) # Saída: Olá, mundo! Eu sou um texto com multiplas linhas e vou ser impresso aqui!

# (\") = Para adicionar aspas no texto (caracter escape \)
# (\n) = Para adicionar uma nova linha no texto
