# 4. Vamos calcular quantos % das vendas o meu top 5 produtos representa das vendas totais

produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça',
            'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte',
            'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450,
          800]
top5 = ['agua', 'brahma', 'skol', 'coca', 'leite de castanha']


vendas_por_produto = dict(zip(produtos, vendas))

vendas_top5 = [vendas_por_produto[produto] for produto in vendas_por_produto if produto in top5]

porcentagem = sum(vendas_top5) / sum(vendas)

print('A porcentagem dos top 5 produtos sobre as vendas representam {:.2%}'.format(porcentagem))
