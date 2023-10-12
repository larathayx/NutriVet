quant = int(input("Digite a quantidade de pets que você quer na lista: "))
pets = []

for x in range(quant):
    nome_tutor = input("Digite o seu nome: ")
    email_tutor = input("Digite o seu e-mail: ")
    senha_tutor = input("Defina a sua senha de acesso: ")
    nome = input("Digite o nome do seu Pet: ")
    idade = input("Digite a idade do seu Pet: ")
    comprimento = input("Digite o comprimento do seu Pet: ")
    raca = input("Digite a raça do seu Pet: ")
    massa = input("Digite o peso do seu Pet (ex: 8.100): ")

    pets_info = {
        'Nome': nome,
        'Idade': idade,
        'Comprimento': comprimento,
        'Raca': raca,
        'Peso': massa,
        'Tutor': nome_tutor,
        'Email': email_tutor,
        'Senha': senha_tutor
    }

    pets.append(pets_info)

with open('dados_NutriVet.txt', 'w') as arquivo:
    for pet in pets:
        arquivo.write(f"Tutor: {pet['Tutor']} , Email: {pet['Email']} , Senha: {pet['Senha']} , Nome: {pet['Nome']} , Idade: {pet['Idade']} , Peso: {pet['Peso']} , Comprimento: {pet['Comprimento']} , Raca: {pet['Raca']}\n")

with open('dados_NutriVet.txt', 'r') as arquiv:
    conteudo = arquiv.read()
    print(conteudo)

def atualizar_conta(pet, campo, novo_valor):
    if campo == 'Nome':
        pet['Nome'] = novo_valor
    elif campo == 'Idade':
        pet['Idade'] = novo_valor
    elif campo == 'Peso':
        pet['Peso'] = novo_valor
    elif campo == 'Comprimento':
        pet['Comprimento'] = novo_valor
    elif campo == 'Tutor':
        pet['Tutor'] = novo_valor
    elif campo == 'Email':
        pet['Email'] = novo_valor
    elif campo == 'Senha':
        pet['Senha'] = novo_valor
    elif campo == 'Raca':
        pet['Raca'] = novo_valor

def atualizar_dados(pets):
    nome_tutor = input("Digite o nome do tutor da conta que deseja atualizar: ")

    for pet in pets:
        if pet['Tutor'] == nome_tutor:
            print(f'Encontrado tutor: {nome_tutor}')
            campo = input("Digite o nome do campo que deseja atualizar (Nome, Idade, Peso, Comprimento, Raca, Email, Senha): ").capitalize()
            if campo in pet:
                novo_valor = input(f"Digite o novo valor para {campo}: ")
                atualizar_conta(pet, campo, novo_valor)
                print(f'{campo} atualizado com sucesso!')
                return
            else:
                print(f'O campo {campo} não é válido.')
                return
    print(f"Tutor com o nome '{nome_tutor}' não encontrado na lista de contas.")

while True:
    atualiza = input("Deseja atualizar algum dado? (s/n) ")
    if atualiza == 's':
        atualizar_dados(pets)
    else:
        break

def procurar_nome(nome_tutor, pets):
    for pet in pets:
        if pet["Tutor"] == nome_tutor:
            return pet
    return None

while True:
    nome_busca = input("Digite o nome do Tutor da conta que deseja encontrar (ou 'sair' para encerrar): ")

    if nome_busca == 'sair':
        break

    conta_encontrada = procurar_nome(nome_busca, pets)

    if conta_encontrada:
        print(f'Tutor: {conta_encontrada["Tutor"]}')
        print(f'Email: {conta_encontrada["Email"]}')
        print(f'Senha: {conta_encontrada["Senha"]}')
        print(f'Nome: {conta_encontrada["Nome"]}')
        print(f'Idade: {conta_encontrada["Idade"]}')
        print(f'Peso: {conta_encontrada["Peso"]}')
        print(f'Comprimento: {conta_encontrada["Comprimento"]}')
        print(f'Raca: {conta_encontrada["Raca"]}')
    else:
        print(f'Conta com o tutor "{nome_busca}" não encontrada.')

def remover_conta(nome_tutor, pets):
    for pet in pets:
        if pet["Tutor"] == nome_tutor:
            pets.remove(pet)
            return True
    return False

def atualizar_arquivo(pets):
    with open('dados_NutriVet.txt', 'w') as arquivo:
        for pet in pets:
            arquivo.write(f"Tutor: {pet['Tutor']} , Email: {pet['Email']} , Senha: {pet['Senha']} , Nome: {pet['Nome']} , Idade: {pet['Idade']} , Peso: {pet['Peso']} , Comprimento: {pet['Comprimento']} , Raca: {pet['Raca']}\n")

while True:
    nome_remover = input("Digite o nome do Tutor da conta a ser removida (ou 'sair' para encerrar): ")
    if nome_remover == 'sair':
        break

    if remover_conta(nome_remover, pets):
        print(f'A conta com o tutor "{nome_remover}" foi removida com sucesso.')
        atualizar_arquivo(pets)
    else:
        print(f'Conta com o tutor "{nome_remover}" não encontrada.')

def adicionar_conta(pets):
    nome_tutor = input("Digite o seu nome: ")
    email_tutor = input("Digite o seu e-mail: ") 
    senha_tutor = input("Defina a sua senha de acesso: ")
    nome = input("Digite o nome do seu Pet: ")
    idade = input("Digite a idade do seu Pet: ")
    comprimento = input("Digite o comprimento do seu Pet: ")
    raca = input("Digite a raça do seu Pet: ")   
    massa = input("Digite o peso do seu Pet (ex: 8.100): ") 

    nova_conta = {
        'Nome': nome,
        'Idade': idade,
        'Comprimento': comprimento,
        'Raca': raca,
        'Peso': massa,
        'Tutor': nome_tutor,
        'Email': email_tutor,
        'Senha': senha_tutor
    }

    pets.append(nova_conta)

    with open('dados_NutriVet.txt', 'w') as arquivo: 
        for e in pets:
            arquivo.write(f"Tutor: {e['Tutor']} , Email: {e['Email']} , Senha: {e['Senha']} , Nome: {e['Nome']} , Idade: {e['Idade']} , Peso: {e['Peso']} , Comprimento: {e['Comprimento']} , Raca: {e['Raca']}\n")

while True:
    resposta = input("Deseja adicionar um novo contato? (s/n): ")
    if resposta.lower() != 's':
        break
    adicionar_conta(pets)
