from database import *
from helpers import validaData, validaCPF, validaHora
import datetime

class Agendamento:

    def criar_tabela():
        try:
            dml('''CREATE TABLE "agendamentos" (
                "id"	INTEGER NOT NULL UNIQUE,
                "cpf"	TEXT NOT NULL,
                "data"	TEXT NOT NULL,
                "hora"	TEXT NOT NULL,
                "status"	TEXT NOT NULL DEFAULT 'R',
                PRIMARY KEY("id" AUTOINCREMENT)
            )''')
        except Exception as e:
            print(f'[x] Falha ao criar tabela [x]: {e}')
        else:
            print('[!] Tabela criada com sucesso [!]\n')

    def cadastra(cpf, data, hora):
        data_registro = data
        hora_registro = int(hora.split(':')[0])

        agendamentos = dql(f"SELECT * FROM agendamentos WHERE data='{data_registro}' AND status='R'")
        if len(agendamentos) > 7:
            print("Limite de agendamentos atingido")
            return True

        if (hora_registro < 8 or hora_registro > 17 or hora_registro == 12):
            print("Agendamento fora do horário, agenda entre 08:00 e 17:00")
            return True

        agendado = False
        for agenda in agendamentos:
            if hora in agenda:
                agendado = True
        
        if agendado:
            print(f"Já existe agendamento no horario: {hora}")
            return True

        dml(f"INSERT INTO agendamentos (cpf, data, hora) VALUES ('{cpf}', '{data}', '{hora}')")
        
        return dql(f"SELECT MAX(id) AS ID FROM agendamentos")[0][0]

    def lista(filtros):
        filtro = ''
        if filtros != None:
            if 'cpf' in filtros:
                if len(filtros['cpf']) > 0:
                    filtro = f"cpf='{filtros['cpf']}' AND "
            if 'data' in filtros:
                if len(filtros['data']) > 0:
                    filtro = f"data='{filtros['data']}' AND "

        agendamentos = dql(f"SELECT * FROM agendamentos WHERE {filtro} status='R'")
        if len(agendamentos) <= 0:
            return ''

        return agendamentos 

    def excluir(id):
        return dml(f"DELETE FROM agendamentos WHERE id={id}")

    def validar(validaInput, validaValor):
        if validaInput == "cpf":
            return validaCPF(validaValor)

        if validaInput == "data":
            if validaData(validaValor):
                return True
        
        if validaInput == "hora":
            return validaHora(validaValor)
        
        return False