# ## 3. Criando um mini sistema de controle de estoque

# - Crie um sistema para ser usado pelo time de controle de estoque de um
# centro de distribuição.
# - Imagine que ao fim de todo dia, o time conta quantas unidades de produto
# existem no estoque. Se tivermos um estoque abaixo do estoque permitido para
# aquela categoria do produto, o time deve ser avisado (print) para fazer um
# novo pedido daquele produto.
# - Cada categoria de produto tem um estoque mínimo diferente, segundo a regra
# abaixo:

# - alimentos -> Estoque mínimo: 50
# - bebidas -> Estoque mínimo: 75
# - limpeza -> Estoque mínimo: 30

# Para isso vamos criar um programa que pede 3 inputs do usuário: nome do
# produto, categoria e quantidade atual em estoque.

# Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa
# deve printar a mensagem
# "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"

# Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa
# não deve exibir nenhuma mensagem.<br>
# Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa
# deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas
# 60 unidades em estoque.

# Obs: lembre de usar o int() para transformar o número inserido pelo usuário
# no input de string para int.<br>
# Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve
# exibir uma mensagem para avisá-lo de preencher corretamente.
# """

# #seu código aqui

estoque_alimentos = 50
estoque_bebidas = 75
estoque_limpeza = 30


def checar_estoque(produto, estoque_minimo, unidades):
    if unidades < estoque_minimo:
        message = f"Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque."
        print(message)


def coletar_informacoes():
    segmento = input("Insira o segmento do produto: ")
    produto = input("Insira o tipo de produto: ")
    unidades = input("Insira a quantidade disponível em estoque: ")

    if segmento and produto and unidades:
        if segmento == "alimentos":
            checar_estoque(produto, estoque_alimentos, int(unidades))
        elif segmento == "bebidas":
            checar_estoque(produto, estoque_bebidas, int(unidades))
        elif segmento == "limpeza":
            checar_estoque(produto, estoque_limpeza, int(unidades))
        else:
            print("Segmento não identificado.")
    else:
        print("Preencha todos os campos.")


coletar_informacoes()
