### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

lista_usuario = list()
usuario1 = {'Nome': 'Antonio', 'Senha': '12345'}
usuario2 = {'Nome': 'Rafaela', 'Senha': ''}
usuario3 = {'Nome': 'Yesmin', 'Senha': '12345'}

lista_usuario.append(usuario1)
lista_usuario.append(usuario2)
lista_usuario.append(usuario3)

usuario3.values


usuario_invalido = list()
for x in lista_usuario:
    if x['Senha'] == '':
        print(x)

# usuarios_validaos = [usuarios for usuarios in lista_usuario if usuarios['Senha']] #Estudar sobre List Comprehension (Compreensão de Listas) para entender esta solução.

# print(usuarios_validaos)

