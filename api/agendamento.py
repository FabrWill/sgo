import sqlite3
from sqlite3 import Error
from helpers import Helpers
from datetime import datetime

class Agendamento:

    def __init__(self, data=None, id=None, filtros={}):
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
        self.data = data
        self.id = id
        self.filtros = filtros

        # self.criar_tabela()
        pass

    def __del__(self):
        self.cur.close()

    '''
    def criar_tabela(self):
        try:
            self.cur.execute('CREATE TABLE "agendamentos" (
                "id"	INTEGER NOT NULL UNIQUE,
                "cpf"	TEXT NOT NULL,
                "data"	TEXT NOT NULL,
                "hora"	TEXT NOT NULL,
                "status"	TEXT NOT NULL DEFAULT 'R',
                PRIMARY KEY("id" AUTOINCREMENT)
            )')
        except Exception as e:
            print(f'[x] Falha ao criar tabela [x]: {e}')
        else:
            print('[!] Tabela criada com sucesso [!]\n')
    '''

    def cadastra(self):
        data = self.data
        
        data_registro = data['data']
        hora_registro = int(data['hora'].split(':')[0])

        query = f"SELECT * FROM agendamentos WHERE data='{data_registro}' AND status='R'"
        res = self.cur.execute(query)
        agendamentos = res.fetchall()
        if len(agendamentos) > 7:
            return Helpers.response(400, 'Limite de agendamentos atingido')

        print(hora_registro)
        if (hora_registro < 8 or hora_registro > 17 or hora_registro == 12):
            return Helpers.response(400, 'Agendamento fora do horário, agenda entre 08:00 e 17:00')

        agendado = False
        for agendamento in agendamentos:
            if data['hora'] in agendamento:
                agendado = True
        
        if agendado:
            return Helpers.response(400, 'Já existe agendamento no horario: ' + data['hora'])

        res = self.cur.execute("INSERT INTO agendamentos (cpf, data, hora) VALUES (?,?,?)", (data['cpf'], data['data'], data['hora']))
        self.con.commit()
        return data

    def listar(self):
        fiiltro = '' 
        if len(self.data['cpf']) > 0:
            filtro = f"cpf='{self.data['cpf']}' AND "

        query = f"SELECT * FROM agendamentos WHERE {filtro} status='R'"
        res = self.cur.execute(query)
        agendamentos = res.fetchall()
        if len(agendamentos) <= 0:
            return Helpers.response(400, 'Sem agendamentos cadastrados')

        return agendamentos

    def confirmar(self):
        print(self.id)
        self.cur.execute("DELETE FROM agendamentos WHERE id=?", (self.id))
        self.con.commit()
        return self.id
