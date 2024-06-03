Assuntos abordados: Type Hint, listas e dicionários.


# O Type Hint (Dica de Tipo) serve apenas para identificar o tipo de determinada variável. No entanto, ele não garante que a mesma será do tipo indiciado. Por tanto, ainda assim, serão necessárias outras abordagens para validação, como a função isinstance(), por exemplo.

# Exemplos de Type HInt: após o nome da variável colocar ":" e o tipo.
idade: int = 0 
preco: float = 5.6
nome: str = "Fatima"
status: bool = True

# Exemplos de isinstance()
text = "Olá, mundo!"
print(isinstance(text, str))  # Saída: True

# Estrutura de dados Complexos

# Lista []


# Dicionário {}
Semelhante com a lista, porém trabalha com "chave - valor". É possível acrescentar um  ou mais dicionários em uma lista

# Tupla ()