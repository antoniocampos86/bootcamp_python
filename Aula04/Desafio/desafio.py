nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    try:
        nome = input("Por favor, informe o seu nome: ")
        if nome.isnumeric():
            raise ValueError("Você digitou um número.")
        
        elif len(nome) == 0:
            raise ValueError("A informação do seu nome é obrigatóra.")
        
        elif nome.isspace():
            raise ValueError("Você digitou espaço ao invés do seu nome.")
        else:
            nome_valido = True        
            # print("Nome válido.")

    except ValueError as teste:
        print(teste)    
      #  exit()    

while salario_valido is not True:
    try:
        salario = float(input("Por favor, nos informe o seu salário: "))
        if salario < 0:
            print("Você passou o valor menor que zero.")
        else:
            salario_valido = True
            # print("Salário Válido")            
    except ValueError :
        print("Entrada inválida para o salário. Por favor, digite um número.")
        # exit()

while bonus_valido is not True:  
    try:
        bonus = float(input("Agora, nos diga a porcentagem do bônus recebido: "))  
        if bonus < 0:
            print("Digite um valor positivo para o bônus.")
        else:
            bonus_valido =True
            # print("Bonus Valido")
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
        # exit()

kpi = 1000 + salario * bonus

# #Usando a concatenação
# print("Olá "+ nome +", o seu valor bônus foi de R$",kpi)

#Usando F String. ":.2f" se trata de um "modificador" e neste exemplo Indica que o resultado final apresentará duas casas decimais.
print(f"Olá {nome}, o seu valor bônus é de R$ {kpi:.2f}")