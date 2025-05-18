""" Manipulação de arquivos
Na análise de dados, podemos usar Python para trabalhar com outros arquivos!

O tratamento de entrada/saída (E/S) de arquivos nos permite interagir com arquivos externos para vários propósitos, incluindo:

  Salvar informações em um arquivo escrevendo nele.
 Ler um arquivo para usar suas informações.
 Manutenção do sistema de arquivos do seu computador.
 
Vamos nos aprofundar nos aspectos práticos do manuseio de arquivos, incluindo operações comuns e manuseio de diferentes formatos, como CSV.

O open()método é sua porta de entrada para manipular arquivos em Python! """

# This opens example file for writing
file = open('example.txt', 'w')

#Neste exemplo, você especifica o nome do arquivo e como deseja tratá-lo (por exemplo, leitura ou gravação). O open()método pode criar ou abrir um arquivo, dependendo das condições.
#Podemos escrever neste fileobjeto de exemplo com o .write()método:

file.write('Hello, World! 🌎')

#Se você executar o código acima, um novo arquivo example.txt com o texto será criado no seu computador!

# Abrindo arquivos
Ao manusear um arquivo, você precisa abri-lo primeiro. 🔑

Em Python, usamos a open()função:

file = open(file_path, mode)

Esta função retorna um objeto que podemos salvar em uma variável como file.

A open()função recebe dois argumentos:

O file_path, como 'filename.txt'.
Como modeusar o arquivo.
Existem três modos para abrir um arquivo:

'r'para ler um arquivo. 📖
'w'para escrever em um arquivo. ✍🏼
'a'para escrever a partir do final de um arquivo. 📝
Observação: Tenha cuidado com 'w'o modo. Ele substituirá qualquer conteúdo de arquivo existente. Use 'a'para evitar isso.

# Escrevendo em arquivos
Você pode gravar em um arquivo com vários métodos. O write()método simplesmente grava dados em um arquivo:

file.write('text')

Uma string é passada para o write()método e gravada no arquivo.

Para escrever em várias linhas, este método deve ser usado várias vezes com o \ncaractere de nova linha:

file.write('This is a line.\n')
file.write('This is the next line.\n')

Você também pode escrever várias linhas em um arquivo de uma só vez com o writelines()método:

lines = ['This is a line.\n', 'This is the next line.\n']

file.writelines(lines)

O writelines()método pega uma lista de linhas e as grava no arquivo.

# Lendo Arquivos
Para ler arquivos, você também tem opções.

O .read()método permite ler todo o conteúdo de um arquivo. Este método pode ser salvo em uma variável e impresso no terminal:

file = open('filename.txt', 'r')

content = file.read()

print('Using read():')
print(content)

O .readline()método permite que você leia um arquivo uma linha por vez:

line1 = file.readline()  # Read the first line
print(line1, end='')     # Printing the first line

line2 = file.readline()  # Read the second line
print(line2, end='')     # Printing the second line

Para imprimir cada linha em uma única linha sem adicionar um '\n'caractere de nova linha no final, usamos a end=''opção na print()função.

Nota: Por padrão, print()termina com um '\n'caractere de nova linha.

O .readlines()método permite que você leia todas as linhas de uma lista:

lines = file.readlines()

for line in lines:
  print(line, end='')

# Fechando Arquivos
Em Python, o .close()método é usado para terminar de trabalhar com um arquivo e liberar recursos.

# Opens file to read
file = open('filename.txt', 'r')

# Closes file
file.close()

Sempre ligue .close()depois de ler ou gravar no arquivo para garantir que tudo foi salvo.

Você também pode usar um withbloco para abrir um arquivo, manipulá-lo e fechá-lo automaticamente:

with open('filename', 'r') as f:
  # handle file here

Não .close()é necessário nenhum método!
