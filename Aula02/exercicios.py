import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# numero_01 = int(input("Informe um número: "))
# numero_02 = int(input("Informe outro número: "))
# resultado = numero_01 + numero_02
# print(f"O resultado da soma entre os números '{numero_01}' e '{numero_02}' é {resultado}")


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# try:
#     numero = int(input("Infome um valor: "))
#     resultado = numero % 5
#     print(f"O resto da divisão de {numero} por 5 é: {resultado}")
# except TypeError:
#     print("O valor informado não é do tipo inteiro. Impossível fazer a operação desejada.")
# except ZeroDivisionError:
#     print("Não é possível realizar uma divisão por zero!")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# numero_01 = int(input("Informe um número: "))
# numero_02 = int(input("Informe outro número: "))
# resulado = numero_01 * numero_02
# print(f"O resultado do valor '{numero_01}' muplicador pelo valor '{numero_02}' é: {resulado}")


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# try:
#     divisor = int(input("Informe um número: "))
#     dividento = int(input("Informe outro número: "))
#     resultado = divisor // dividento
#     print(f"o resultado da divisão é {resultado}")
# except ZeroDivisionError:
#     print("Onde já se viu dividir algum número por ZERO, rapá?!")


# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero_01 = int(input("Informe um número: "))
# quadrado = numero_01 ** 2
# print(f"{numero_01} elevado ao quadrado é: {quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero_01 = float(input("Informe um numero decimal: "))
# numero_02 = float(input("Informe um numero decimal: "))
# resultado = numero_01 + numero_02
# print(f"Resultado da soma: {resultado:.3f}")


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero_01 = float(input("Informe um numero decimal: "))
# numero_02 = float(input("Informe um numero decimal: "))
# resultado = (numero_01 + numero_02) / 2 
# print(f"A médida dos números {numero_01} e {numero_02} é: {resultado}")


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# print("Vamos calulcar potência? :D")
# base = float(input("Por favor, informe a base: "))
# expoente = float(input("Agora, informe o expoente: "))
# potencia =  base ** expoente
# print(f"O valor da potência é {potencia}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Informe a temperatura em Celsius: "))
# fahrenheit = celsius * 1.8 + 32
# print(f"A temperatura {celsius} graus Celsius, equivale à {fahrenheit:.1f} graus Fahrenheit")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Por favor, informe o valor do raio: "))
# perimento = math.pi * raio ** 2
# print(f"A área do círculo é {perimento:.1f}")



# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# palavra = input("Escreva alguma palavra: ")
# print(f"Palavra escrita com letras maisúculas: {palavra.upper()}")


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# palavra = input("Escreva alguma palavra: ")
# print(f"Palavra escrita com letras minúsculas: {palavra.lower()}")


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Escreva frase: ")
# print(frase.strip())


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Informe uma data no formato 'DD/MM/YYYY': ")
# lista_data = data.split("/")
# print(f"Dia: {lista_data[0]}")
# print(f"Mês: {lista_data[1]}")
# print(f"Ano: {lista_data[2]}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# primeiro_nome = input("Informe o seu primeiro nome: ")
# ultimo_nome = input("Agora, seu último nome: ")
# print("Nome completo: ", primeiro_nome + ultimo_nome)



# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação