import sqlite3
from sqlite3 import Error
from helpers import Helpers

class Servico:

    def __init__(self, data={}, id=None, filtros={}):
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
            self.cur.execute('''CREATE TABLE "servicos" (
                "id"	INTEGER NOT NULL UNIQUE,
                "descricao"	TEXT NOT NULL,
                "preco"	REAL NULL,
                "quantidade"	INTEGER NULL,
                "data"	TEXT NULL,
                "cpf"	TEXT NULL,
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

        res = self.cur.execute("INSERT INTO servicos (descricao, preco, quantidade, data, cpf) VALUES (?,?,?,?,?)", (data['descricao'], data['preco'], data['quantidade'], data['data'], data['data']))
        self.con.commit()

        return data

    def listar(self):
        filtro = '' 
        if "cpf" in self.data:
            if len(self.data['cpf']) > 0:
                filtro = f"WHERE cpf='{self.data['cpf']}' "

        query = f"SELECT * FROM servicos {filtro}"
        res = self.cur.execute(query)
        agendamentos = res.fetchall()
        if len(agendamentos) <= 0:
            return Helpers.response(400, 'Sem servicos cadastrados')

        return agendamentos

    def total(self):
        query = "SELECT (SUM(preco)*quantidade) AS TOTAL, (SUBSTR(data, 6,2)||'/'||SUBSTR(data, 1,4)) AS MES FROM servicos GROUP BY SUBSTR(data, 0, 8)"
        res = self.cur.execute(query)
        agendamentos = res.fetchall()
        if len(agendamentos) <= 0:
            return Helpers.response(400, 'Sem servicos cadastrados')

        return agendamentos