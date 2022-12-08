from flask import Flask, request, jsonify
#from database import *
from helpers import Helpers
from cliente import Cliente
from agendamento import Agendamento
from servico import Servico

app = Flask('SGO')


@app.route('/', methods=['GET'])
def home():
    return {'no-data': 'sem registro da rota'}

#### CLIENTES ####
# /clientes?escluidos=S/N&buscar=nome/cpf -> Traz todos os clisntes em ordem alfabetica
@app.route('/clientes', methods=['GET'])
def getClientes():
    filtros = {
        "excluidos": request.args.get('excluidos'),
        "buscar": request.args.get('buscar')
    }

    clientes = Cliente(filtros=filtros).lista()
    return Helpers.response(400, 'Lista de Clientes', 'clientes', clientes)

# /cliente/<id> -> Traz as informações do cliente pelo ID
@app.route('/cliente/<id>', methods=['GET'])
def getCliente(id=0):
    if id == 0:
        return Helpers.response(400, 'Cliente não informado')

    cliente = Cliente(id=id).cliente()
    return Helpers.response(400, 'Cliente Atualizado', 'cliente', cliente)

# /cliente -> Cadastra um novo cliente
@app.route('/cliente', methods=['POST'])
def postCliente():
    body = request.get_json()
        
    cliente = Cliente(body).cadastra()
    if cliente == None:
        return Helpers.response(400, 'Erro ao cadastrar cliente')

    return Helpers.response(400, 'Cliente cadastrado', 'cliente', cliente)

# /cliente/<id> -> Atualiza dados do cliente pelo ID
@app.route('/cliente/<id>', methods=['PUT'])
def putCliente(id=0):
    body = request.get_json()

    if id == 0:
        return Helpers.response(400, 'Cliente não informado')

    cliente = Cliente(body, id).atualiza()
    return Helpers.response(400, 'Cliente Atualizado', 'cliente', cliente)

# /cliente/<id> -> Exclui cliente pelo ID
@app.route('/cliente/<id>', methods=['DELETE'])
def deleteCliente(id=0):
    if id == 0:
        return Helpers.response(400, 'Cliente não informado')

    cliente = Cliente(id=id).deleta()
    return Helpers.response(400, 'Cliente Atualizado', 'cliente', cliente)


#### AGENDAMENTO ####
# /agendamento -> Cadastra um novo agendamento
@app.route('/agendamento', methods=['POST'])
def postAgendamento():
    body = request.get_json()
    agendamento = Agendamento(data=body).cadastra()
    return Helpers.response(400, 'Agendamento Cadastrado', 'agendamento', agendamento)

# /agendamento/<cpf>/cancelar -> Cancelar agendamentos
@app.route('/agendamento/<cpf>/cancelar', methods=['GET'])
def getAgendados(cpf):
    body = request.get_json()
    body['cpf'] = cpf

    agendamentos = Agendamento(data=body).listar()
    return Helpers.response(400, 'Agendamentos', 'agendamentos', agendamentos)

# /agendamento/<id>/confirmaCancela -> Confirma o cancelamento do agendamento
@app.route('/agendamento/<id>/cancelar', methods=['DELETE'])
def deleteAgendamento(id):
    if id == 0:
        return Helpers.response(400, 'Agendamento não informado')

    agendamento = Agendamento(id=id).confirmar()
    return Helpers.response(400, 'Agendamentos', 'agendamento', agendamento)

# /agendamentos -> Traz todos os agendamentos
@app.route('/agendamentos', methods=['GET'])
def getAgendamentos():
    agendamentos = Agendamento().listar()
    return Helpers.response(400, 'Agendamentos', 'agendamentos', agendamentos)

# /agendamentos/<cpf> -> Traz os agendamentos de um usuario
@app.route('/agendamentos/<cpf>', methods=['GET'])
def getAgendamentosCpf(cpf):
    body = {'cpf': cpf}

    agendamentos = Agendamento(data=body).listar()
    return Helpers.response(400, 'Agendamentos', 'agendamentos', agendamentos)


#### SERVIÇOS ####
@app.route('/servicos', methods=['POST'])
def postServicos():
    body = request.get_json()

    servicos = {
        'Clínica Geral': 150,
        'Clareamento': 250,
        'Tratamento de Canal': 350,
        'Implanete Dentário': 500
    }

    if body['servico'] not in servicos:
        return Helpers.response(400, 'Serviço não disponível')
    

    return ''

@app.route('/receita', methods=['GET'])
def getReceita():
    receita = Servico().total()
    return Helpers.response(400, 'Servicos', 'servicos', receita)

@app.route('/servicos/<cpf>', methods=['GET'])
def getServicosCpf(cpf):
    body = {'cpf': cpf}

    servicos = Servico(data=body).listar()
    return Helpers.response(400, 'Servicos', 'servicos', servicos)



app.run();
