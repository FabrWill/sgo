import sqlite3
from sqlite3 import Error
from helpers import Helpers

class Cliente:

    def __init__(self, data=None, id=None, filtros={}):
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
        self.data = data
        self.id = id
        self.filtros = filtros

        self.criar_tabela()
        pass

    def __del__(self):
        self.cur.close()

    def criar_tabela(self):
        try:
            self.cur.execute('''CREATE TABLE "clientes" (
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

    def cadastra(self):
        data = self.data
        validar = self.validar()
        if validar != True:
            return validar

        res = self.cur.execute("INSERT INTO clientes (nome, nascimento, cpf, estado_civil, sexo) VALUES (?,?,?,?,?)", (data['nome'], data['nascimento'], data['cpf'], data['estado_civil'], data['sexo']))
        self.con.commit()

        return data

    def atualiza(self):
        validar = self.validar()
        if validar != True:
            return validar

        data = self.data

        res = self.cur.execute("UPDATE clientes SET nome=?, nascimento=?, cpf=?, estado_civil=?, sexo=? WHERE id=?", (data['nome'], data['nascimento'], data['cpf'], data['estado_civil'], data['sexo'], self.id))
        self.con.commit()
        return data

    def deleta(self):
        res = self.cur.execute("UPDATE clientes SET excluido=1 WHERE id=?", (self.id))
        self.con.commit()
        return self.id

    def lista(self):
        filtros = self.filtros

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

        query = f"SELECT * FROM clientes WHERE excluido={excluidos} {buscar} ORDER BY nome ASC"
        res = self.cur.execute(query)
        return res.fetchall()

    def cliente(self):
        id = self.id

        query = f"SELECT * FROM clientes WHERE id={id}"
        res = self.cur.execute(query)
        return res.fetchone()

    def validar(self):
        body = self.data
        if ('nome' not in body):
            return Helpers.response(400, 'O parametro nome é obrigatório')

        if ('nascimento' not in body):
            return Helpers.response(400, 'O parametro nascimento é obrigatório')

        if ('cpf' not in body):
            return Helpers.response(400, 'O parametro cpf é obrigatório')

        if (Helpers.validaCPF(body['cpf'])):
            return Helpers.response(400, 'O cpf é inválido')

        if ('estado_civil' not in body):
            return Helpers.response(400, 'O parametro estado_civil é obrigatório')

        if (body['estado_civil'] not in ['S', 'C', 'V']):
            return Helpers.response(400, 'O estado_civil deve ser (S, C ou V)')

        if ('sexo' not in body):
            return Helpers.response(400, 'O parametro sexo é obrigatório')

        if (body['sexo'] not in ['M', 'F']):
            return Helpers.response(400, 'O sexo deve ser (M, F)')

        return True
