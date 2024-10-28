#Programação Orientada a Objeto estilo Python

#Class
#Syntaxe

""" Modelo básico
vendedor = "Lira"
vendas = 1000
meta = 500

if vendas >= meta:
    print('Bateu a meta')
else:
    print('Não bateu a meta') """

#Usado Classes e Objetos 
class Vendedor():
    def __init__(self, nome): #Init de iniciar para dar todas as caracteristicas que o objeto precisa. 
        self.nome = nome
        self.vendas = 0 

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, 'Bateu a meta!')
        else:
            print(self.nome, 'Não bateu a meta!')

vendedor1 = Vendedor('Lira')
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)

vendedor2 = Vendedor('Alon')
vendedor2.vendeu(300)
vendedor2.bateu_meta(600)

#Outros Exemplos
class Computador:
    def __init__(self,  marca, memoria_ram, procesador, placa_de_video):

        self.marca = marca
        self.memoria_ram = memoria_ram
        self.processador = procesador
        self.placa_de_video = placa_de_video
    pass

computador1 = Computador('HP', '16gb', 'intel core i3', 'Nvidia')
computador2 = Computador('Dell', '500gb', 'AMD Ryzen 5', 'AMD')
computador3 = Computador('Sansung','32gb', 'Intel Core i7', 'Nvidia')

print('\nComputadores em Promoção:')
print(f'{computador1.marca}, {computador1.memoria_ram}, {computador1.placa_de_video}') 
print(f'{computador2.marca}, {computador2.memoria_ram}, {computador2.placa_de_video}') 
print(f'{computador3.marca}, {computador3.memoria_ram}, {computador3.placa_de_video}') 

#Aqui estamos criando objetos e atribuindo valores para eles.

class Computador:
    def __init__(self,  marca, memoria_ram, procesador, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.processador = procesador
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('Aguarde estamos preparando tudo pra você!')

    def Desligar(self):
        print('Obrigada por vir! Desligando...')

    def ExibirConfigurações(self):
        print(self.marca, self.memoria_ram, self.processador, self.placa_de_video) #Escopo

computador1 = Computador('Windows', '16gb', 'Intel Core i7', 'Nvidia')
computador1.Ligar()
computador1.ExibirConfigurações()
computador1.Desligar() 

# Herança
#Base, Pai, Super
class Animal:
    def __init__(self, nome, classe, cor):
        self.nome = nome
        self.classe = classe
        self.cor = cor

class Cobra(Animal):
    def __init__(self, nome, veneno):
        super().__init__(nome, 'Réptil', 'Fatal')  # Define classe como 'Réptil' e cor como 'Desconhecida' para cobras
        self.veneno = veneno

print("Classe de Animais")
animal1 = Animal('Leão', 'Mamífero', 'Amarelo')
print(f"Lista um: {animal1.nome}, {animal1.classe}, {animal1.cor}")

animal2 = Cobra('Coral', 'Veneno Forte')
print(f"Lista dois: {animal2.nome}, {animal2.classe}, {animal2.cor}, {animal2.veneno}")
#Aqui estamos criando uma classe pai e uma classe filha.