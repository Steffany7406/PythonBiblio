#Usando listas
alunos = ['Steffany', 'Saulo', 'Allan', 'Wesley', 'Diana', 'Fernando']
#             0          1        2        3        4          5 
#            -6        -5          -4        -3       -2       -1        
#print(alunos)

#print(alunos[2]) - Passando o indice para acessar o segundo item da lista
#print(alunos[-6]) - Pegando o item de trás para frente
#print(alunos[2:]) - pegando o item de indice 2 até o final da lista

#Alterando item da lista
#print(alunos)
alunos[2] = 'João' #Trocando a posição 2 pela string 'João'
#print(alunos)

#Adionando valores a lista
alunos.extend(['Thais', 'Germano']) #Adicionando outra lista
#print(alunos)

alunos.append("Daiana") #adiciona um valor no final da lista
#print(alunos)

#Inserindo valor no meio da lista e alterando as posições
alunos.insert(3, 'Luis') #Inserindo o valor 'Luis'
#print(alunos)

#Removendo valores da lista
alunos.pop()  #Removendo o último valor da lista sempre
alunos.remove('Saulo') #Removendo com base na direção que ele recebe

#Removendo TODOS  os valores da lista
alunos.clear() #Apaga todos os indices da lista

#Retornando o indice com base no valor
print(alunos.index('Fernando')) #Retorna o indice do valor 'Fernando'

#Retornando e contando a quantidade de valores
print(alunos.count('Fernando'))

#Abrindo novo indice usando números inteiros
#Funciona tanto com número tanto com string
idade_alunos = [24, 33, 35, 26, 25, 34]
#print(idade_alunos)
idade_alunos.sort() #Organizando a lista em ordem crescente

#Executando inverso
idade_alunos.reverse()
#print(idade_alunos) - Retornando a lista em ordem inversa

#Ordenando de trás para frente
idade_alunos.sort() #primeiro ordenando
idade_alunos.reverse() #e depois invertendo

#Copiando uma lista
alunos2 = alunos #uma copia de referência sem criar nova lista
print(alunos2)
#Vamos dizer que nós decidimos remover a string 'Wesley' da lista
#Ele altera a lista original

#Modificando e mantendo uma cópia de segurança
alunos2 =  alunos.copy() #Copia de segurança
#Você compara as duas listas e vê que elas são diferentes