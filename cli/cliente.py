from database import *
from helpers import validaCPF

class Cliente:

    def criar_tabela():
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

    def cadastra(cli = {}):
        return dml(f"INSERT INTO clientes (nome, nascimento, cpf, estado_civil, sexo) VALUES ('{cli['nome']['texto']}','{cli['nascimento']['texto']}','{cli['cpf']['texto']}','{cli['estado_civil']['texto']}','{cli['sexo']['texto']}')")

    def atualiza(cli = {}):
        return dml(f"UPDATE clientes SET nome='{cli['nome']['texto']}', nascimento='{cli['nascimento']['texto']}', cpf='{cli['cpf']['texto']}', estado_civil='{cli['estado_civil']['texto']}', sexo='{cli['sexo']['texto']}' WHERE id='{cli['id']['texto']}'")

    def deleta(id):
        return dml(f"UPDATE clientes SET excluido=1 WHERE id='{id}'")

    def lista(filtros):
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

    def cliente(id):
        return dql(f"SELECT * FROM clientes WHERE id={id}")

    def validar(validaInput, validaValor):
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