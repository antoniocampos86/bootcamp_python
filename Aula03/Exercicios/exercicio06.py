### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "Estou estudando bastante. Quero crescer ainda mais na vida! na na na na"
lista_de_palavras = texto.split() #Cria uma lista contedendo cada palavra do texto.
dicionario = {}

for palavra in lista_de_palavras:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

for c, v in dicionario.items():
    print(f"A palavra '{c}' é apresentada {v} vez(es) no texto informado.")

