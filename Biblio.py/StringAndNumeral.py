#Variaveis = espaços de armazenamento e memória
nome = "Steffany" #String
idade = 24 #numeral inteiro
gosto_de = "programação"

#Imprimindo frases
# F String = Uma forma de formatação de string usando chaves
#print(f"Meu nome é {nome}") 
#print(f"{nome} tem {idade} e gosta de {gosto_de}")

#Int = Para número inteiro
#Float = Para número decimal
idade = 24 

#input = para interação com terminal (usuário)
#nome1 = input("Digite seu nome:")

num1 = 5 
num2 = 3.5

#Função type = para ver o tipo de dado que você está utilzando.
#print(type(num1)) Saida:  <class 'int'>
#print(type(num2)) Saida:   <class 'float'>

#Convertendo variaveis
#Nós indicamos as variaveis e pedimos a conversão ao sistema
a = float(num1)
#print(a)  Saida: 5.0

# Na conversão de um float para um inteiro, o número decimal é cortado e o primeiro é arredondado.
b = int(num2)
#print(b) Saida: 3

#Convertendo string em numeral (int, float)
c = "5"
d = "3.5"
e = int(c)
#print(e) Saida: 5
f = float(d)
#print(f) Saida: 3.5

# Se tentarmos converter uma string que não é um numeral, o sistema irá gerar um erro.
# A mesma coisa para tentar converter uma string float para int, se o número tiver um decimal, o sistema irá gerar um erro.
#Exemplo: a = int(3.5) = Saída Erro: ValueError: could not convert string to float: '3.5'
#Para resolver usamos: a = int(float(a)) = Primeiro ele converte para Float e depois para inteiro.