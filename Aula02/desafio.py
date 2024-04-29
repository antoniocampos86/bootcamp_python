try:
    nome = input("Por favor, informe o seu nome: ")
    if nome.isnumeric():
        raise ValueError("Você digitou um número. Procedimento abortado!")
        
    elif len(nome) == 0:
        raise ValueError("A informação do seu nome é obrigatóra. Procedimento abortado!")
        
    elif nome.isspace():
        raise ValueError("A informação do seu nome é obrigatóra. Procedimento abortado!(2)")        

except ValueError as teste:
    print(teste)    
    exit()    

try:
    salario = float(input("Por favor, nos informe o seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
        
except ValueError :
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()
  
try:
    bonus = float(input("Agora, nos diga a porcentagemdo bônus recebido: "))  
    if bonus < 0:
        print("Digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

kpi = 1000 + salario * bonus

    # #Usando a concatenação
    # print("Olá "+ nome +", o seu valor bônus foi de R$",kpi)

    #Usando F String. ":.2f" se trata de um "modificador" e neste exemplo Indica que o resultado final apresentará duas casas decimais.
print(f"Olá {nome}, o seu valor bônus foi de R$ {kpi:.2f}")