# 4. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

str1 = 'Brasil Hexa 2006'
str2 = 'Brasil! Hexa 2006!'

str1_len = len(str1)
str2_len = len(str2)

def print_str(str, len):
    print(f'Tamanho de {str}: {len} caracteres')

def compare_str(str1, str2, message1, message2):
    if str1 == str2:
        print(message1)
    else:
        print(message2)

print_str(str1, str1_len)
print_str(str2, str2_len)
compare_str(str1_len, str2_len, 'As duas strings são de tamanhos iguais', 'As duas strings são de tamanhos diferentes')
compare_str(str1, str2, 'As duas strings possuem conteúdo iguais', 'As duas strings possuem conteúdo diferente')
