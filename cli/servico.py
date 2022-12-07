#import sqlite3
#from sqlite3 import Error
#from helpers import Helpers
from database import *
from helpers import validaData, validaCPF, validaHora
import datetime

class Servico:

    def criar_tabela():
        try:
            dml('''CREATE TABLE "servicos" (
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

    def cadastra(data = {}):
        result = dml(f"INSERT INTO servicos (descricao, preco, quantidade, data, cpf) VALUES ('{data['descricao']['valor']}','{data['preco']['valor']}','{data['quantidade']['valor']}','{data['data']['valor']}','{data['cpf']['valor']}')")

        return result

    def listar(data = {}):
        fiiltro = '' 
        if len(data['cpf']) > 0:
            filtro = f"WHERE cpf='{data['cpf']}' "

        agendamentos = dql(f"SELECT * FROM servicos {filtro}")
        if len(agendamentos) <= 0:
            print("Sem servicos cadastrados")
            return False

        return agendamentos

    def total():
        agendamentos = dql("SELECT (SUM(preco)*quantidade) AS TOTAL, (SUBSTR(data, 6,2)||'/'||SUBSTR(data, 1,4)) AS MES FROM servicos GROUP BY SUBSTR(data, 0, 8)")
        if len(agendamentos) <= 0:
            print('Sem servicos cadastrados')
            return False

        return agendamentos
    
    def validar(validaInput, validaValor):
        if validaInput == "cpf":
            return validaCPF(validaValor)

        if validaInput == "data":
            if validaData(validaValor):
                return True

        if validaInput == "quantidade":
            return int(validaValor) < 0
        
        return False