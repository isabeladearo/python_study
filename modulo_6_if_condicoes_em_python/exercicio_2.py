# ## 2. Cálculo de bônus com uma nova regra

# - Agora, crie um novo código que calcule e dê um print no bônus dos
# funcionários novamente. Porém há uma nova regra nesse 2º caso:

# A meta é 1000 vendas<br>
# Agora, os funcionários que venderem muito acima da meta ganham mais
# bônus do que os outros. Então o bônus é definido da seguinte forma:<br>

# - Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15%
#     sobre o valor de vendas
# - Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então
#     o bônus é de 10% sobre o valor de vendas
# - Se vendas funcionário for menos do que 1000 então o bônus do funcionário é
#     de 0.

# Use as mesmas variáveis de vendas_funcionários
# """

# #crie seu código aqui

meta = 1000
vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700


def calculo_bonus(porcentagem, vendas):
    return round((porcentagem / 100) * vendas)


def calculo_bonus_funcionario(codigo, vendas, meta):
    if vendas >= meta and vendas >= 2000:
        bonus = calculo_bonus(15, vendas)
        print(f"O funcionário {codigo} ganhou {bonus} de bônus")
    elif vendas >= meta and vendas < 2000:
        bonus = calculo_bonus(10, vendas)
        print(f"O funcionário {codigo} ganhou {bonus} de bônus")
    else:
        print(f"O funcionário {codigo} ganhou 0 de bônus")


calculo_bonus_funcionario(1, vendas_funcionario1, meta)
calculo_bonus_funcionario(2, vendas_funcionario2, meta)
calculo_bonus_funcionario(3, vendas_funcionario3, meta)

# """Resposta:
# O funcionário 1 ganhou 100 de bônus
# O funcionário 2 ganhou 0 de bônus
# O funcionário 3 ganhou 405 de bônus
# """
