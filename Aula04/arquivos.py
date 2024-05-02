import csv

caminho_do_arquivo = "exemplo_csv.csv"
arquivo_csv: list = []

# print(arquivo_csv)

# informo o caminho, digo que quero ler (r) e passo o esquema de codificação (utf-8) - opciional
with open(file=caminho_do_arquivo, mode="r",encoding="utf-8") as arquivo:
# crio uma variavel para receber o conteudo lido no arquivo que estamos trabalhando
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)
        