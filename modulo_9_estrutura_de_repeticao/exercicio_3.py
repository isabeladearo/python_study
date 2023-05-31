# 3. Comparação com Ano Anterior
# Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.

# Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.

# Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)

# Dica: lembre do enumerate, ele pode facilitar seu "for"

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

crescimento_sob_vendas = []

def formatar_custo(custo):
    return 'R${:_.2f}'.format(custo).replace('.', ',').replace('_', '.')

for i, venda in enumerate(vendas2020):
    crescimento = round((venda - vendas2019[i]) / vendas2019[i] * 100, 2)
    crescimento_sob_vendas.append([f"2019: {formatar_custo(vendas2019[i])}",f"2020: {formatar_custo(venda)}", f"{crescimento}%"])

for venda in crescimento_sob_vendas:
    print(venda)
