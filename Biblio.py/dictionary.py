#Dicionários são coleções não ordenadas que permitem armazenar e acessar dados com pares key:value

dictionary = {key: value} # single line

dictionary = { # multi-line
  key1: value1,
  key2: value2,
  key3: value3
}

#Os pares key: valuesão separados por vírgulas e cercados por chaves { }.
#Com listas e tuplas, acessamos seus itens por índice. Já com dicionários, acessamos seus itens por chave. 🔑

laptop = {
  'brand': 'Apple',
  'model': 'Macbook Pro',
  'size': 14,
  'year': 2023
}

#Cada chave em um dicionário deve ser única e associada a um valor específico. Esse pareamento permite uma recuperação eficiente de dados. As chaves também devem ser imutáveis, como uma string.
#Para acessar o valor associado a uma chave específica em um dicionário, use [ ]colchetes com a chave dentro.

print(laptop['model']) # Output: Macbook Pro

#Considere um cenário em que você está gerenciando um banco de dados de artefatos ou pessoas, cada um com informações exclusivas. Vamos definir um dicionário!

student_info = {'name': 'Alice', 'age': 9, 'grade': 'A'} # Creating a dictionary

# Accessing dictionary elements
print('Name:', student_info['name'])
print('Age:', student_info['age'])
print('Grade:', student_info['grade'])

# Modifying dictionary elements
student_info['age'] = 10
print('Updated Age:', student_info['age'])

# Métodos de Dicionário
#Os dicionários vêm equipados com vários métodos para agilizar tarefas comuns. Isso inclui .keys(), .values(), e items():

# Dictionary methods
print('Keys:', student_info.keys())
print('Values:', student_info.values())
print('Items:', student_info.items())

#Isso imprime o seguinte:

Keys: dict_keys(['name', 'age', 'grade'])
Values: dict_values(['Alice', 9, 'A'])
Items: dict_items([('name', 'Alice'), ('age', 9), ('grade', 'A')])

#.keys()retorna apenas as chaves de um dicionário.
#.values()retorna apenas os valores.
#.items()retorna uma lista de pares chave-valor como tuplas.
#À medida que você continua sua jornada no Python, tenha em mente as maneiras como os dicionários podem simplificar seu código e otimizar seus programas.

#Example: 

met_museum = {
  'name': 'Mangaakaa',
  'culture': 'Congo',
  'date': 'Century XIX',
  'class': 'wood-sculpture'
}
print("Printing the Key: ", met_museum['name'])
