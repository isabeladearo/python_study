# 2. Data Science e Inteligência Artificial usa MUITO isso.
#
# Quando criamos um modelo de previsão, precisamos treinar esse modelo e testar para ver se ele sendo um bom modelo
# ou não. Temos então que pegar os nossos dados e dividir em 2 pedaços, uma lista de treino e uma lista de teste.
# Vamos então pensar no exemplo de um modelo que tenta identificar qual o valor justo de um imóvel conforme o
# tamanho do imóvel. Temos então 2 listas:
# Lista 1: Preços Reais dos Imóveis
# Lista 2: Tamanho do imóvel.
# Vamos criar então uma função que recebe 2 listas como entrada e que divide cada uma dessas listas em 2,
# um pedaço de treino e um pedaço de teste. O percentual que a lista vai ser dividida é definida por um fator
# (que também vai ser um parâmetro da função)

valor_dos_imoveis = [2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37]
tamanho_dos_imoveis = [207, 148, 130, 203, 257, 228, 160, 194, 232, 147]


def modelo_imoveis(lista, fator) -> tuple:
    i = int((1 - fator) * len(lista))
    lista_treino = lista[:i]
    lista_teste = lista[i:]
    return lista_treino, lista_teste


def extrair_modelo_imoveis(lista1, lista2, fator) -> tuple:
    if len(lista1) != len(lista2):
        print("Listas com tamanhos diferentes, por favor, corrija.")
    else:
        return modelo_imoveis(lista1, fator), modelo_imoveis(lista2, fator)


valor, tamanho = extrair_modelo_imoveis(valor_dos_imoveis, tamanho_dos_imoveis, 0.1)
valor_treino, valor_teste = valor
tamanho_treino, tamanho_teste = tamanho

print("Valor:")
print(valor_treino)
print(valor_teste)
print("")
print("Tamanho:")
print(tamanho_treino)
print(tamanho_teste)
