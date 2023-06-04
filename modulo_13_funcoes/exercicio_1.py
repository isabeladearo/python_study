# 1. Cálculo do Percentual e da Lista de Vendedores
# Queremos criar uma function que consiga identificar os vendedores
# que bateram uma meta, mas, além disso, consigo já me dar como resposta o cálculo do % da lista de vendedores que
# bateu a meta (para eu não precisar calcular manualmente depois) Essa function deve receber 2 informações como
# parâmetro: a meta e um dicionário com os vendedores e suas vendas. E me dar 2 respostas: uma lista com o nome dos
# vendedores que bateram a meta e o % de vendedores que bateu a meta.

meta = 10000

vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}


def checar_vendedores(vendedores, meta_desejada):
    vendedores_com_meta_batida = []

    for vendedor in vendedores:
        if vendedores[vendedor] >= meta_desejada:
            vendedores_com_meta_batida.append(vendedor)

    porcentagem = len(vendedores_com_meta_batida) / len(vendedores)

    return vendedores_com_meta_batida, '{:.0%}'.format(porcentagem)


vendedores_selecionados, porcentagem_vendedores = checar_vendedores(vendas, meta)
print(vendedores_selecionados)
print(porcentagem_vendedores)
