# 1. Calculando % de uma lista
# Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

# Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.

# Vamos resolver de 2 formas:
# 1- Criando uma lista auxiliar apenas com os vendedores que bateram a meta
# 2- Fazendo o cálculo diretamente na lista que já temos

# Para treinar uma estrutura parecida, crie um código para responder: quem foi o vendedor que mais vendeu?

meta = 10000
vendas = [
    ["João", 15000],
    ["Julia", 27000],
    ["Marcus", 9900],
    ["Maria", 3750],
    ["Ana", 10300],
    ["Alon", 7870],
]

vendedores = []

for venda in vendas:
    if venda[1] >= meta:
        vendedores.append(venda)

porcentagem = len(vendedores) / len(vendas)
print("{:.0%} bateram a meta".format(porcentagem))

vendedor = ""
valor = 0

for venda in vendas:
    if venda[1] > valor:
        vendedor = venda[0]
        valor = venda[1]

print(
    "{} foi o vendedor que bateu a maior meta: de R$ {:.2f}".format(
        vendedor, valor
    )
)
