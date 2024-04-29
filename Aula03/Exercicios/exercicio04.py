### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input("Por favor, informe a sua idade: "))
email = input("Agora, o seu e-mail: ")

# Variavei de teste
# idade = 17
# email = "antonio_cff@hotmail.com"

validacao_email = email.find("@",)

if idade < 18 or idade > 65:
    print("A sua idadade não permite acesso.")   
elif validacao_email == -1:
    print(f"o e-mail {email} é inválido.")
else:
    print("Dados de usuário válidos.")





