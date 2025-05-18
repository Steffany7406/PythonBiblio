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
