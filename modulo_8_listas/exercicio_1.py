# ## 1. Faturamento do Melhor e do Pior Mês do Ano

# Qual foi o valor de vendas do melhor mês do Ano?
# E valor do pior mês do ano?
# """

meses = [
    "jan",
    "fev",
    "mar",
    "abr",
    "mai",
    "jun",
    "jul",
    "ago",
    "set",
    "out",
    "nov",
    "dez",
]
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_totais = vendas_1sem + vendas_2sem

min_vendas = min(vendas_totais)
index_min_vendas = vendas_totais.index(min_vendas)
pior_mes = meses[index_min_vendas]

max_vendas = max(vendas_totais)
index_max_vendas = vendas_totais.index(max_vendas)
melhor_mes = meses[index_max_vendas]

print("O pior mês de venda foi: {}, com R${:.2f}".format(pior_mes, min_vendas))
print(
    "O melhor mês de venda foi: {}, com R${:.2f}".format(
        melhor_mes, max_vendas
    )
)
