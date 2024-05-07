### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

lista_usuario = list()
usuario1 = {'Nome': 'Antonio', 'Senha': '12345'}
usuario2 = {'Nome': 'Rafaela', 'Senha': ''}
usuario3 = {'Nome': 'Yasmin', 'Senha': '12345'}

lista_usuario.append(usuario1)
lista_usuario.append(usuario2)
lista_usuario.append(usuario3)

usuario3.values


usuario_invalido = list()
usuario_valido = list()
for x in lista_usuario:
    if x['Senha'] == '':
        usuario_invalido.append(x)
    else:
        usuario_valido.append(x)

usuarios_validados = [usuarios for usuarios in lista_usuario if usuarios['Senha']] #Estudar sobre List Comprehension (Compreensão de Listas) para entender esta solução.

print(f"Usuários invalidos: {usuario_invalido} ")
print(f"Usuários válidos: {usuario_valido} ")
print(usuarios_validados)

