# ## 1. Cadastro de CPF

# Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input box apenas com números.

# Ex: 'Insira seu CPF (digite apenas números)'

# Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"
# """

cpf = input("Insira seu CPF (digite apenas números):").strip()

if not cpf.isnumeric() or len(cpf) < 11:
    print("Digite seu CPF corretamente e digite apenas números")
else:
    print(f"CPF: {cpf}")
