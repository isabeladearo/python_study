# ## 4. Mudança de Carga Tributária

# - Reformas e mudanças de cargas tributárias são bem comuns no Brasil.

# Digamos que você trabalhe em uma empresa de ecommerce

# No Brasil, o imposto sobre livros é zerado. De um ano para o outro, o governo criou um novo imposto que incide em 10% sobre o valor dos livros e agora você precisa alterar o registro dos preços dos livros da empresa para garantir que esse imposto vai ser repassado para o preço final do produto.

# Crie um código que recalcule o valor do livro da sua lista de produtos e ajuste na tabela.

# Além disso, calcule qual vai ser o impacto financeiro da criação desse imposto para a empresa (ou seja, quanto que o imposto vai aumentar de custo para a empresa)

# Obs: para facilitar, colocamos apenas 1 livro na lista, mas em breve vamos aprender um for que vai adaptar esse cenário para qualquer quantidade de livros na sua lista.

# Obs2: Seu código deve funcionar mesmo que não haja livros na lista de produtos da empresa
# """

# cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem

# ATENÇÃO: resolvi criar um código que mostre o aumento de 10% de imposto para cada produto, independente de ser livro ou não

produtos = [
    "computador",
    "livro",
    "tablet",
    "celular",
    "tv",
    "ar condicionado",
    "alexa",
    "máquina de café",
    "kindle",
]

produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400],
]

print(f"Lista sem aplicação do imposto: {produtos_ecommerce}")


def calcular_custo_por_produto(lista):
    custo_por_produto = []
    for i in range(len(lista)):
        custo_por_produto.append(lista[i][0] * lista[i][1])
    return custo_por_produto


def calcular_custo_de_estoque(lista):
    custo_por_produto = calcular_custo_por_produto(produtos_ecommerce)
    return sum(custo_por_produto)


def formatar_custo(custo):
    return "R${:_.2f}".format(custo).replace(".", ",").replace("_", ".")


custo_estoque_sem_ajuste = calcular_custo_de_estoque(produtos_ecommerce)
print(
    f"Custo de estoque sem aplicação de imposto: {formatar_custo(custo_estoque_sem_ajuste)}"
)


def calcule_novo_preco(lista):
    for i in range(len(lista)):
        novo_custo = round(lista[i][1] * 1.1)
        lista[i][1] = novo_custo


calcule_novo_preco(produtos_ecommerce)
print("Lista ajustada ao imposto: {}".format(produtos_ecommerce))

custo_estoque_com_ajuste = calcular_custo_de_estoque(produtos_ecommerce)
print(
    f"Custo de estoque com ajuste de imposto: {formatar_custo(custo_estoque_com_ajuste)}"
)

diferenca_custo_de_estoque = (
    custo_estoque_com_ajuste - custo_estoque_sem_ajuste
)
print(
    f"O aumento do custo de estoque para a empresa será de: {formatar_custo(diferenca_custo_de_estoque)}"
)
