# """## 2. Continuação

# Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

# Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

# Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
# """

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_totais = vendas_1sem + vendas_2sem

min_vendas = min(vendas_totais)
index_min_vendas = vendas_totais.index(min_vendas)
pior_mes = meses[index_min_vendas]

max_vendas = max(vendas_totais)
index_max_vendas = vendas_totais.index(max_vendas)
melhor_mes = meses[index_max_vendas]

faturamento_total = sum(vendas_totais)
porcentagem_melhor_mes = max_vendas / faturamento_total

print('O faturamento anual foi de : R${:.2f}'.format(faturamento_total))
print('O pior mês de venda foi: {}, com R${:.2f}'.format(pior_mes, min_vendas))
print('O melhor mês de venda foi: {}, com R${:.2f}, correspondendo a {:.2%} do faturamento anual'.format(melhor_mes, max_vendas, porcentagem_melhor_mes))
