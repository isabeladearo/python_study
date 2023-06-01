# 5. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

numero = input("Insira o número de telefone:").strip().replace("-", "")

if len(numero) == 7:
    print(
        "Telefone possui 7 dígitos. Vou acrescentar o digito três na frente."
    )
    novo_numero = f"3{numero}"
    print(f"Telefone corrigido sem formatação: {novo_numero}")
    print(
        f"Telefone corrigido com formatação: {novo_numero[:4]}-{novo_numero[4:]}"
    )
else:
    print("Insira um número com 7 dīgitos")
