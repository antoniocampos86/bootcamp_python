### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

lista_de_numeros = [1,2,3,4,5,6,7,8]
lista_de_numeros_pares = list()
lista_de_numeros_impares = list()

for x in lista_de_numeros:
    if x % 2 == 0:
        lista_de_numeros_pares.append(x)
    else:
        lista_de_numeros_impares.append(x)

print(f"Lista de números pares: {lista_de_numeros_pares}")
print(f"Lista de números impares: {lista_de_numeros_impares}")