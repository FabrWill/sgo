import os

from database import *
from agendamento import *
from cliente import *
from servico import *
from helpers import validaData, validaCPF

baseDir = os.path.dirname(__file__)


def cadastraCliente():
    print("--- CADASTRAR CLIENTE ---")

    cliente = {
        "nome": {"texto": "Nome Completo: ", "valor": ""},
        "nascimento": {"texto": "Data de Nascimento: ", "valor": ""},
        "cpf": {"texto": "CPF: ", "valor": ""},
        "estado_civil": {"texto": "Estado Civil (S, C, V): ", "valor": ""},
        "sexo": {"texto": "Sexo (M, F): ", "valor": ""},
    }
    for valido in cliente.keys():
        while cliente[valido]["valor"] == "":
            cliente[valido]["valor"] = input(cliente[valido]["texto"]).upper()

            if Cliente.validar(valido, cliente[valido]["valor"]):
                cliente[valido]["valor"] = ""

    Cliente.cadastra(cliente)
    print("----> Cliente Cadastrado!")
    acao = int(input("Deseja cadastrar outro cliente ? (1 - Sim, 0 - Não): "))
    if acao == 1:
        cadastraCliente()

    main()

def cadastraAgendamento():
    print("--- CADASTRAR AGENDAMENTO ---")
    
    data = input("Digite uma data para consultar disponibilidade: ")
    while validaData(data):
        data = input("Digite uma data para consultar disponibilidade: ")

    indisponiveis = Agendamento.lista({"data": data});
    if len(indisponiveis) > 0:
        print("--- HORÁRIOS INDISPONÍVEIS ---")
        for indisponivel in indisponiveis:
            print(f"{indisponivel[3]}")
    else:
        print("--- TODOS OS HORÁRIOS DISPONÍVEIS ---")
    
    agendamento = {
        "cpf": {"texto": "Digite o CPF do cliente: ", "valor": ""},
        "data": {"texto": "Digite a Data do agendamento: ", "valor": ""},
        "hora": {"texto": "Digite a Hora do agendamento: ", "valor": ""},
    }
    for valido in agendamento.keys():
        while agendamento[valido]["valor"] == "":
            agendamento[valido]["valor"] = input(agendamento[valido]["texto"]).upper()

            if Agendamento.validar(valido, agendamento[valido]["valor"]):
                agendamento[valido]["valor"] = ""

    cadastro = Agendamento.cadastra(agendamento["cpf"]["valor"], agendamento["data"]["valor"], agendamento["hora"]["valor"])
    if cadastro:
        print(f"O agendamento (id:{cadastro}) foi realizado!")
    
        acao = int(input("Deseja cadastrar outro agendamento ? (1 - Sim, 0 - Não): "))
        if acao == 1:
            cadastraAgendamento()

    print("ERRO NO CADASTRO")
    main()

def cancelaAgendamento():
    print("--- CANCELAR AGENDAMENTO ---")

    cliente = {
        "cpf": {"texto": "Digite o CPF do Cliente: ", "valor": ""},
    }
    for valido in cliente.keys():
        while cliente[valido]["valor"] == "":
            cliente[valido]["valor"] = input(cliente[valido]["texto"]).upper()

            if Cliente.validar(valido, cliente[valido]["valor"]):
                cliente[valido]["valor"] = ""

    agendamentos = Agendamento.lista({"cpf": cliente["cpf"]["valor"]});
    if len(agendamentos) > 0:
        print("----> LISTA DE AGENDAMENTOS!")
        print("COD  |  DATA  |  HORA  ")
        cod_agendamento = [];
        for agendamento in agendamentos:
            print(f"{agendamento[0]}  |  {agendamento[2]}  |  {agendamento[3]}")
            cod_agendamento.append(agendamento[0])
    else:
        print("--- SEM AGENDAMENTOS REGISTRADOS ---")
        acao = int(input("Deseja consultar outro cliente ? (1 - Sim, 0 - Não): "))
        if acao == 1:
            cancelaAgendamento()
        main()

    cancelar = int(input("Digite o código do agendamento para cancelar: "))
    while cancelar not in cod_agendamento:
        print("--- CÕDIGO INVÁLIDO ---")
        cancelar = input("Digite o código do agendamento para cancelar: ")
    Agendamento.excluir(cancelar)

    acao = int(input("Deseja cancelar outro agendamento? (1 - Sim, 0 - Não): "))
    if acao == 1:
        cancelaAgendamento()

    main()

def cadastroServico():
    servico = {
        "quantidade": {"texto": "Digite a quantidade: ", "valor": ""},
        "data": {"texto": "Digite a Data do serviço: ", "valor": ""},
        "cpf": {"texto": "Digite o CPF do cliente: ", "valor": ""},
    }
    
    print("--- CADASTRAR SERVIÇOS ---")

    servicos = {
        "1": {"nome": "Clínica Geral", "valor": 150.00},
        "2": {"nome": "Clareamento", "valor": 250.00},
        "3": {"nome": "Tratamento de Canal", "valor": 350.00},
        "4": {"nome": "Implante Dentário", "valor": 500.00},
    }
    print("COD  |  SERVIÇO  |  VALOR  ")
    for serv in list(servicos.keys()):
        print(f"{serv} |  {servicos[serv]['nome']}  |  {servicos[serv]['valor']}  ")

    servicoSelecionado = input("Escolha um código de serviço: ")
    while servicoSelecionado not in list(servicos.keys()):
        print("--- Serviço inválido ---")
        print("COD  |  SERVIÇO  |  VALOR  ")
        for serv in list(servicos.keys()):
            print(f"{serv} |  {servicos[serv]['nome']}  |  {servicos[serv]['valor']}  ")

        servicoSelecionado = input("Escolha um código de serviço: ")

    for valido in servico.keys():
        while servico[valido]["valor"] == "":
            servico[valido]["valor"] = input(servico[valido]["texto"]).upper()

            if Servico.validar(valido, servico[valido]["valor"]):
                servico[valido]["valor"] = ""

    if servicoSelecionado in list(servicos.keys()):
        servico.update({"descricao": {"texto": " ", "valor": servicos[servicoSelecionado]["nome"]}})
        servico.update({"preco": {"texto": " ", "valor": servicos[servicoSelecionado]["valor"]}})

    Servico.cadastra(servico)

    acao = int(input("Deseja cadastrar outro serviço? (1 - Sim, 0 - Não): "))
    if acao == 1:
        cadastroServico()

    main()

def relatorioAgendamentos():
    print("1. Relatório de todos os agendamentos.")

    agendamentos = Agendamento.lista({})
    print("CPF  |  DATA  |  HORA")
    for agendamento in agendamentos:
        print(f"{agendamento[1]}  |  {agendamento[2]} |  {agendamento[3]}  ")
        print("")

    acao = int(input("Deseja gerar outro relatorio? (1 - Sim, 0 - Não): "))
    if acao == 1:
        relatorioAgendamentos()

    main()

def cpfAgendamentos():
    print("2. Relatório de agendamentos por pessoa (pesquisar por CPF).")
    cpf = input("Digite o CPF de um cliente: ")

    agendamentos = Agendamento.lista({"cpf": cpf})
    print("CPF  |  DATA  |  HORA")
    for agendamento in agendamentos:
        print(f"{agendamento[1]}  |  {agendamento[2]} |  {agendamento[3]}  ")
        print("")

    acao = int(input("Deseja gerar outro relatorio? (1 - Sim, 0 - Não): "))
    if acao == 1:
        cpfAgendamentos()

    main()

def relatorioMes():
    print("3. Relatório de receita total por mês.")

    servicos = Servico.total()
    print("MES  | TOTAL  ")
    for servico in servicos:
        print(f"{servico[1]}  |  {servico[0]}  ")
        print("")

    acao = int(input("Deseja gerar outro relatorio? (1 - Sim, 0 - Não): "))
    if acao == 1:
        relatorioMes()

    main()

def relatorioServicos():
    print("4. Relatório serviços prestado por pessoa (pesquisar por CPF).")
    cpf = input("Digite o CPF de um cliente: ")

    servicos = Servico.listar({"cpf": cpf})
    print("DESCRIÇÃO  |  PREÇO  |  QTD  | DATA  ")
    for servico in servicos:
        print(f"{servico[1]}  |  {servico[2]}  |  {servico[3]}  | {servico[4]}  ")
        print("")

    acao = int(input("Deseja gerar outro relatorio? (1 - Sim, 0 - Não): "))
    if acao == 1:
        relatorioServicos()

    main()

def relatorios():
    os.system("clear")
    print("---------- RELATORIOS ----------")
    print("Selecione o relatorio no menu abaixo")
    print("1. Relatório de todos os agendamentos.")
    print("2. Relatório de agendamentos por pessoa (pesquisar por CPF).")
    print("3. Relatório de receita total por mês.")
    print("4. Relatório serviço prestado por pessoa (pesquisar por CPF).")
    print("6. Sair.")
    menu = int(input("Digite o código do relatorio: "))

    programas = [
        "--",
        "relatorioAgendamentos",
        "cpfAgendamentos",
        "relatorioMes",
        "relatorioServicos"
    ]

    if menu in [1,2,3,4]:
        os.system("clear")
        eval(programas[menu] + "()")
    else:
        exit()


def main():
    os.system("clear")
    print("---------- SGO ----------")
    print("Selecione o programa no menu abaixo")
    print("1. Cadastrar cliente.")
    print("2. Realizar agendamento.")
    print("3. Cancelar agendamento.")
    print("4. Cadastro de serviço.")
    print("5. Relatórios.")
    print("6. Sair.")
    menu = int(input("Digite o código do programa: "))

    programas = [
        "--",
        "cadastraCliente",
        "cadastraAgendamento",
        "cancelaAgendamento",
        "cadastroServico",
        "relatorios"
    ]

    if menu in [1,2,3,4,5]:
        os.system("clear")
        eval(programas[menu] + "()")
    else:
        exit()

main()