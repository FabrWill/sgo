from tkinter import *

from agenda import tkNovaAgenda, tkPesquisaAgenda, tkExcluiAgenda
from cliente import tkNovoCliente, tkPesquisaCliente, tkExcluiCliente

def semComando():
    return ''

app = Tk()
app.title('SGO - Sistema Gestão Odontológica')
app.geometry('800x600')

barraDeMenus = Menu(app)
menuClientes = Menu(barraDeMenus, tearoff=False)
menuClientes.add_command(label="Novo", command=tkNovoCliente)
menuClientes.add_command(label="Pesquisar", command=tkPesquisaCliente)
menuClientes.add_command(label="Deletar", command=tkExcluiCliente)

menuAgendamentos = Menu(barraDeMenus, tearoff=False)
menuAgendamentos.add_command(label="Novo", command=tkNovaAgenda)
menuAgendamentos.add_command(label="Pesquisar", command=tkPesquisaAgenda)
menuAgendamentos.add_command(label="Deletar", command=tkExcluiAgenda)

menuServicos = Menu(barraDeMenus, tearoff=False)
menuServicos.add_command(label="Novo", command=semComando)
menuServicos.add_command(label="Pesquisar", command=semComando)

menuRelatorios = Menu(barraDeMenus, tearoff=False)
menuRelatorios.add_command(label="Agendamentos", command=semComando)
menuRelatorios.add_command(label="Agendamentos por Cliente", command=semComando)
menuRelatorios.add_command(label="Receita Total por Mês", command=semComando)
menuRelatorios.add_command(label="Serviços por Cliente", command=semComando)

menuAjuda = Menu(barraDeMenus, tearoff=False)
menuAjuda.add_command(label="Sobre", command=semComando)
menuAjuda.add_command(label="Versão", command=semComando)
menuAjuda.add_separator()
menuAjuda.add_command(label="Sair", command=app.quit)

barraDeMenus.add_cascade(label="Clientes", menu=menuClientes)
barraDeMenus.add_cascade(label="Agendamentos", menu=menuAgendamentos)
barraDeMenus.add_cascade(label="Serviços", menu=menuServicos)
barraDeMenus.add_cascade(label="Relatõrios", menu=menuRelatorios)
barraDeMenus.add_cascade(label="Ajuda", menu=menuAjuda)
app.config(menu=barraDeMenus)

app.mainloop()
