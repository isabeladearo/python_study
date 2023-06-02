# Digamos que você está analisando as vendas do Banco de Dados de um e-commerce.

# Em um determinado dia, você extraiu as vendas do Banco de Dados e elas vieram nesse formato:

vendas = [
    ("20/08/2020", "iphone x", "azul", "128gb", 350, 4000),
    ("20/08/2020", "iphone x", "prata", "128gb", 1500, 4000),
    ("20/08/2020", "ipad", "prata", "256gb", 127, 6000),
    ("20/08/2020", "ipad", "prata", "128gb", 981, 5000),
    ("21/08/2020", "iphone x", "azul", "128gb", 397, 4000),
    ("21/08/2020", "iphone x", "prata", "128gb", 1017, 4000),
    ("21/08/2020", "ipad", "prata", "256gb", 50, 6000),
    ("21/08/2020", "ipad", "prata", "128gb", 4000, 5000),
]

# Qual foi o faturamento de IPhone no dia 20/08/2020?
# Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?

faturamento = 0
produto = ""
unidades_vendidas = 0

for venda in vendas:
    data, modelo, cor, tamanho, unidades, preco = venda
    if data == "20/08/2020" and modelo == 'iphone x':
        faturamento += unidades * preco
    elif data == "21/08/2020":
        if unidades > unidades_vendidas:
            unidades_vendidas = unidades
            produto = modelo
        else:
            pass
    else:
        pass

print("Faturamento: R${:.2f}".format(faturamento))
print("Produto mais vendido: {} - {} unidades".format(produto, unidades_vendidas))
