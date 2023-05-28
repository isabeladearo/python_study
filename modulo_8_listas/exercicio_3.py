# """## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

top3 = []

vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_totais = vendas_1sem + vendas_2sem

def extrai_maior_valor(vendas):
    maior_valor = max(vendas)
    top3.append(maior_valor)
    vendas_totais.remove(maior_valor)

for i in range(3):
    extrai_maior_valor(vendas_totais)

print(top3)

