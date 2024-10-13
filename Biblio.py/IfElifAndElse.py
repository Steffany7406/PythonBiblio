#If, Else, Statemant é uma estrututa de seleção que vai realizar uma ação com base na seleção
#de uma condição. Se a condição for verdadeira, ele irá realizar a ação definida no If, caso contrário, irá realizar a ação definida no Else

#tenho_sede =  True

#if tenho_sede:
    #print('Beber água')

    #print('Vida que segue')    

#esta_frio = False
#if esta_frio:
   # print('Vestir um casaco')
#else:
  #  print('Vestir camiseta')

#tenho_sede = True
#tenho_fome = False

#if tenho_sede:
    #print('beber água')
#elif tenho_fome: #OBS: O elif é usado para verificar se a condição anterior não foi atendida
    #print('Procurar comida')
#else:
    #print('Voltar a estudar')

"""Outras Formas:
if tenho_sede or tenho_fome:
    print('Ir para a cozinha')
    else:
        print('Voltar a estudar')

if tenho_sede and tenho_fome:
    print('Fazer um sanduiche com coca')
 else:
    print('Voltar a estudar')   
""" 
#-----------------------------------
"""
And(e) = é usado para  verificar se ambas as condições forem verdadeiras
Or(ou) = é usado para verificar se pelo menos uma das condições for verdadeira
Not(negação) = é usado para verificar se a condição for falsa
"""
#-----------------------------------
"""
estou_em_dieta = True

if tenho_sede and tenho_fome:
    print('Fazer um sanduiche com coca')
elif tenho_sede and not(tenho_fome):
    if estou_em_dieta:
        print('Beber água')
    else:
        print('Beber coca')
elif  tenho_fome and not(tenho_sede):
    print('Procurar comida')
else:
    print('Voltar a estudar')
"""

#operadores de comparação
#Serve para números tal qual string

num1 = 25
num2 = 26

if num1 == num2:
    print('Os números são iguais')
elif num1 != num2:
    print('Os números são diferentes')

if num1 < num2:
    print('O primeiro número é menor que o segundo')
elif num1 > num2:
    print('O primeiro número é maior')

if num1 <= num2:
    print('O primeiro número é menor ou igual ao segundo')
elif num1 >= num2:
    print('O primeiro número é maior ou igual ao segundo')

"""Operadores de comparação
== igual a
!= diferente de
< menor que
> maior que
<= menor ou igual a
>= maior ou igual a
"""
