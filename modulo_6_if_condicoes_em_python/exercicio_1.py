# 1. Cálculo de Bônus

# - Crie um programa que calcule e dê um print no bônus que os funcionários
# devem receber segundo a regra:

# A meta é 1000 vendas.<br>
# Se o valor de vendas for maior ou igual a meta, o valor do bônus do
# funcionário é 10% do valor de vendas.<br>
# Caso contrário o valor de bônus do funcionário é 0.<br>
# Print o bônus dos 3 funcionários
# """

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

# #crie seu código aqui

meta = 1000


def calculo_bonus(codigo, vendas, meta):
    if vendas >= meta:
        bonus = 0.1
        bonus_funcionario = round(vendas * bonus)
        print(f"O funcionário {codigo} ganhou {bonus_funcionario} de bônus")
    else:
        print(f"O funcionário {codigo} ganhou 0 de bônus")


calculo_bonus(1, vendas_funcionario1, meta)
calculo_bonus(2, vendas_funcionario2, meta)
calculo_bonus(3, vendas_funcionario3, meta)


# """Resposta:
# O funcionário 1 ganhou 100 de bônus
# O funcionário 2 ganhou 0 de bônus
# O funcionário 3 ganhou 270 de bônus
