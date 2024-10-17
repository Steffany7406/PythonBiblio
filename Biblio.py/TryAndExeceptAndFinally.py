"""
Saber lidar com erros/excessoes é uma parte muito importante da programação independente da linguagem que for, 
sim, nosso programa nem sempre roda como o esperado, você pode receber um tipo de dado que você não estava esperando, 
uma variavel esta vazia, você não abriu o arquivo antes de tentar ler, enfim, diversas coisas podem acontecer 
e geralmente quando isso acontece vc recebe uma mensagem de erro e seu programa para de rodar, 
mas nos podemos lidar com essas falhas inesperadas, 
manter nossa aplicação rodando e ainda mostrar uma mensagem amigavel para o usuário.
"""

#Exemplo simples
try: # = tentativa
    num = int(input("Digite o número que você calça: ")) #Se tentar digitar uma string ele recebe como erro
    print(num)
    10/0
except ZeroDivisionError:    
    print("Divisão por zero não é possivel.")
except:  # = exceção
    print("Valor inválido! Tente novamente!") 
    #Como o IF/Else ele envia uma mensagem de erro e para de executar o anterior. 
finally: # = sempre ou finalmente
    print("Sempre executa.")  
    #mesmo se o programa tiver algum erro ele ainda executa essa parte.
