nome = input("Por favor, informe o seu nome: ")
salario = float(input("Por favor, nos informe o seu salário: "))
bonus = float(input("Agora, nos diga a porcentagemdo bônus recebido: "))

kpi = 1000 + salario * bonus

#Usando a concatenação
print("Olá "+ nome +", o seu valor bônus foi de R$",kpi)

#Usando F String. ":.2f" se trata de um "modificador" e neste exemplo Indica que o resultado final apresentará duas casas decimais.
print(f"Olá {nome}, o seu valor bônus foi de R$ {kpi:.2f}")
