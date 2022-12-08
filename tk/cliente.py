from tkinter.ttk import Combobox

from database import *
from tkinter import *
from helpers import validaCPF

def tkNovoCliente():
    app = Tk()
    app.title('SGO - Novo CLiente')
    app.geometry('800x600')

    Label(app, text="Nome Completo: ", fg='black', anchor=W).place(x=50, y=100, width=800, height=20)
    nome_completo = Entry(app)
    nome_completo.place(x=200, y=100, height=20)

    Label(app, text="Data de Nascimento: ", fg='black', anchor=W).place(x=50, y=130, width=800, height=20)
    nascimento = Entry(app)
    nascimento.place(x=200, y=130, height=20)

    Label(app, text="CPF: ", fg='black', anchor=W).place(x=50, y=160, width=800, height=20)
    cpf = Entry(app)
    cpf.place(x=200, y=160, height=20)

    estado_civil_data = ("S", "C", "V")
    Label(app, text="Estado Civil (S, C, V): ", fg='black', anchor=W).place(x=50, y=190, width=800, height=20)
    estado_civil = Combobox(app, values=estado_civil_data)
    estado_civil.place(x=200, y=190)

    sexo_data = ("M", "F")
    Label(app, text="Sexo (M, F): ", fg='black', anchor=W).place(x=50, y=220, width=800, height=20)
    sexo = Combobox(app, values=sexo_data)
    sexo.place(x=200, y=220)


    cliente = {
        "nome": {"texto": "Nome Completo: ", "valor": nome_completo.get()},
        "nascimento": {"texto": "Data de Nascimento: ", "valor": nascimento.get()},
        "cpf": {"texto": "CPF: ", "valor": cpf.get()},
        "estado_civil": {"texto": "Estado Civil (S, C, V): ", "valor": estado_civil.get()},
        "sexo": {"texto": "Sexo (M, F): ", "valor": sexo.get()},
    }
    def execCadastro(cliente):
        for valido in cliente.keys():
            while cliente[valido]["valor"] == "":
                if Cliente.validar(valido, cliente[valido]["valor"]):
                    cliente[valido]["valor"] = ""

        # Cliente.cadastra(cliente)

    btn = Button(app, text="Gravar", command=(execCadastro(cliente)))
    btn.place(x=30, y=300, height=20)

    app.mainloop()
def tkPesquisaCliente():
    return ''
def tkExcluiCliente():
    return ''

class Cliente:

    def __init__(self):
        return ''

    def criar_tabela(self):
        try:
            dml('''CREATE TABLE "clientes" (
                "id"	INTEGER NOT NULL UNIQUE,
                "nome"	TEXT NOT NULL,
                "nascimento"	TEXT NOT NULL,
                "cpf"	TEXT NOT NULL,
                "estado_civil"	TEXT NOT NULL,
                "sexo"	TEXT NOT NULL,
                "excluido"	INTEGER DEFAULT 'N',
                PRIMARY KEY("id" AUTOINCREMENT)
            )''')
        except Exception as e:
            print(f'[x] Falha ao criar tabela [x]: {e}')
        else:
            print('[!] Tabela criada com sucesso [!]\n')

    def cadastra(self, cli = {}):
        return dml(f"INSERT INTO clientes (nome, nascimento, cpf, estado_civil, sexo) VALUES ('{cli['nome']['texto']}','{cli['nascimento']['texto']}','{cli['cpf']['texto']}','{cli['estado_civil']['texto']}','{cli['sexo']['texto']}')")

    def atualiza(self, cli = {}):
        return dml(f"UPDATE clientes SET nome='{cli['nome']['texto']}', nascimento='{cli['nascimento']['texto']}', cpf='{cli['cpf']['texto']}', estado_civil='{cli['estado_civil']['texto']}', sexo='{cli['sexo']['texto']}' WHERE id='{cli['id']['texto']}'")

    def deleta(self, id):
        return dml(f"UPDATE clientes SET excluido=1 WHERE id='{id}'")

    def lista(self, filtros):
        if filtros != None:
            excluidos = 0
            if 'excluidos' in filtros:
                if filtros['excluidos'] == 'S':
                    excluidos = 1
            
            buscar = ''
            if 'buscar' in filtros:
                if filtros['buscar'] != None:
                    if len(filtros['buscar']) > 0:
                        termo = filtros['buscar'].lower()
                        buscar = 'AND nome LIKE "%'+termo+'%" OR cpf LIKE "%'+termo+'%"'

        return dql(f"SELECT * FROM clientes WHERE excluido={excluidos} {buscar} ORDER BY nome ASC")

    def cliente(self, id):
        return dql(f"SELECT * FROM clientes WHERE id={id}")

    def validar(self, validaInput, validaValor):
        validaValor = validaValor.upper()
        if validaInput == "cpf":
            return validaCPF(validaValor)
                    
        if validaInput == "estado_civil":
            if len(validaValor) > 1:
                print("O estado civil deve ter apenas 1 caracter")
                return True
        
            if validaValor not in ["S", "C", "V"]:
                print("O estado civil deve ser uma das opções")
                return True
        
        if validaInput == "sexo":
            if len(validaValor) > 1:
                print("O sexo deve ter apenas 1 caracter")
                return True
        
            if validaValor not in ["M", "F"]:
                print("O sexo deve ser uma das opções")
                return True
        
        return False