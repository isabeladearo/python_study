# # Exercícios do Módulo 1 - Operações, Variáveis e Input

# ### Parte 1 - Operações e Variáveis
# Crie um programa que imprima (print) os principais indicadores da loja
# Hashtag&Drink no último ano.
# Obs: faça tudo usando variáveis.

# Valores do último ano:

# Quantidade de Vendas de Coca = 150<br>
# Quantidade de Vendas de Pepsi = 130<br>
# Preço Unitário da Coca = 1,50 <br>
# Preço Unitário da Pepsi = 1,50<br>
# Custo da Loja: 2.500,00

# Use o bloco abaixo para criar todas as variáveis que precisar.

qnte_de_vendas_de_coca = 150
qnte_de_vendas_de_pepsi = 130
preco_unitario_da_coca = 1.50
preco_unitario_da_pepsi = 1.50
custo_da_loja = 2500.00

# """1. Qual foi o faturamento de Pepsi da Loja?"""

faturamento_pepsi = qnte_de_vendas_de_pepsi * preco_unitario_da_pepsi
print(f"Faturamento: {faturamento_pepsi}")

# """2. Qual foi o faturamento de Coca da Loja?"""

faturamento_coca = qnte_de_vendas_de_coca * preco_unitario_da_coca
print(f"Faturamento de coca: {faturamento_coca}")

# """3. Qual foi o faturamento da loja?"""

faturamento = faturamento_coca + faturamento_pepsi
lucro = faturamento - custo_da_loja
print(f"Lucro da loja: {lucro}")

# """4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento).
# Não precisa formatar em percentual"""

margem = lucro / faturamento
print(f"Margem: {margem}")
