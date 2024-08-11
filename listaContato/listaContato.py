import re 
import sys
agenda = []
def adicionaContato():
    nome = input("Digite o nome do contato:\n")
    email = input("Digite o email do contato:\n")
    while True:
        numero = input("Digite o número do contato (Apenas o DDD e os 9 números):\n")
        numero = re.sub(r"\D", "", numero)
        if len(numero) != 11:
            print("Número inválido!!")
        else:
            break
    contato = {
        nome: {
            "Email": email,
            "Numero": numero
        }
    }
    agenda.append(contato)

def buscaContato():
    nome = input("Digite o nome do contato ou parte parcial dele:\n")
    for i in agenda:
        for k, v in i.items():
            if k.lower().startswith(nome.lower()):
                print("Nome:", k)
                print("Email:", v["Email"])
                print("Número:", v["Numero"])

def listaContatos():
    for i in agenda:
        for k, v in i.items():
            print("Nome:", k)
            print("Email:", v["Email"])
            print("Número:", v["Numero"])

def editaContato():
    lista = []
    nome = input("Digite o nome do contato ou parte parcial dele:\n")
    contador = 1
    for indice, i in enumerate(agenda):
        for k in i.keys():
            if k.lower().startswith(nome.lower()):
                print(contador, "-", k)
                lista.append((contador, indice))
                contador += 1
    if not lista:
        print("Nenhum contato encontrado")
        return
    contato = input("Digite o valor do contato que deseja editar:\n")
    if not contato.isdigit():
        print("Não é um valor correspondente!!")
        return
    contato = int(contato)
    encontrado = False
    indice = 0
    for i in lista:
        if i[0] == contato:
            encontrado = True
            indice = i[1]
    if not encontrado:
        print("Opção inválida!!")
        return
    while True:
        print("1 - Nome")
        print("2 - Email")
        print("3 - Número")
        print("4 - Salvar alterações\n")
        menu = input("Digite a opção que deseja selecionar\n")
        nome = list(agenda[indice].keys())[0]
        if menu == "1":
            novoNome = input("Digite o novo nome do contato:\n")
            agenda[indice][novoNome] = agenda[indice].pop(nome)
            nome = novoNome
        elif menu == "2":
            email = input("Digite o novo email do contato:\n")
            agenda[indice][nome]["Email"] = email
        elif menu == "3":
            while True:
                numero = input("Digite o novo número do contato (Apenas o DDD e os 9 números):\n")
                numero = re.sub(r"\D", "", numero)
                if len(numero) != 11:
                    print("Número inválido!!")
                else:
                    agenda[indice][nome]["Numero"] = numero
                    break
        elif menu == "4":
            return
        else:
            print("Opção inválida!!")

def removeContato():
    nome = input("Digite o nome do contato ou parte parcial dele:\n")
    contador = 1
    lista = []
    for indice, i in enumerate(agenda):
        for k in i.keys():
            if k.lower().startswith(nome.lower()):
                print(contador, "-", k)
                lista.append((contador, indice))
                contador += 1
    if not lista:
        print("Nenhum contado encontrado")
        return
    contato = input("Digite o valor do contato que deseja remover:\n")
    if not contato.isdigit():
        print("Valor digitado não é válido")
        return
    contato = int(contato)
    encontrado = False
    for i in lista:
        if i[0] == contato:
            remover = i[1]
            encontrado = True
    if not encontrado:
        print("Opção inválida!!")
        return
    agenda.pop(remover)
    print("Contato removido com sucesso!!")

print("Seja bem vindo à agenda")

while True:
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar todos os contatos")
    print("4 - Editar contato")
    print("5 - Remover contato")
    print("6 - Sair")
    menu = input("Selecione uma opção do menu:\n")
    if not menu.isdigit():
        print("O valor deve ser numérico!!")
        continue
    menu = int(menu)
    if menu < 1 and menu > 6:
        print("Selecione uma opção válida!!")
        continue
    if menu == 1:
        adicionaContato()
    elif menu == 2:
        buscaContato()
    elif menu == 3:
        listaContatos()
    elif menu == 4:
        editaContato()
    elif menu == 5:
        removeContato()
    else:
        sys.exit()