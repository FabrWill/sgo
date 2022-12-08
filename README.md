# sgo
Sistema de gerenciamento odontologico - ABP de programação I


## ABP – Aprendizagem Baseada em Projeto

Para a projeto final da disciplina de Programação, a equipe (no máximo 3 alunos) deverá desenvolver um sistema de agendamento de clínica odontológica. O programa deverá ser desenvolvido na linguagem de programação Python. O programa desenvolvido deverá cumprir as seguintes tarefas:

- Menu principal
    - A clínica deverá ter acesso a um menu principal com as seguintes opções:
        1. Cadastrar cliente.
        2. Realizar agendamento.
        3. Cancelar agendamento.
        4. Cadastro de serviço.
        5. Relatórios.
        6. Sair.
    - O programa só deverá ser encerrado caso o usuário escolha a opção de sair.

- Cadastro de Cliente
    - Nessa tela a clínica terá a opção de cadastrar um determinado cliente.
    - Todas as informações abaixo são obrigatórias para o cadastro do cliente.
    - Identificador do cliente (gerar automaticamente, o usuário da clínica não pode mexer nesse campo).
        - Nome completo do cliente.
        - Data de Nascimento
        - CPF.
        - Estado Civil (S – Solteiro, C – Casado, V – Viúvo).
        - Sexo (M – Masculino, F – Feminino)
    - Caso algum dos campos não forem fornecidos, o sistema deverá apresentar uma mensagem de aviso e reiniciar o cadastro.
    - O sistema deverá apresentar uma mensagem de cadastro realizado com sucesso.

- Realizar Agendamento.
    - Nessa tela a clínica terá a opção de realizar um agendamento conforme disponibilidade de agenda.
    - O sistema deve utilizar o CPF para confirmar um agendamento e um cliente pode realizar quantos agendamentos ele quiser.
    - Considere que a agenda é padronizada com agendamentos de 1h e horário de funcionamento das 8h às 12h e das 13h às 17h, ou seja, podem ser realizados até 8 agendamentos por dia de semana de segunda à sexta-feira.
    - O sistema deverá apresentar uma mensagem de agendamento realizado. Ex: ‘O
agendamento (id:8521) foi realizado !!!’.

- Cancelar Agendamento.
    - Nessa tela a clínica terá a opção de cancelar um agendamento. Para isso o usuário deverá realizar a busca pelo CPF do cliente.
        - Caso exista mais de um agendamento no CPF da pessoa, o usuário deverá
escolher qual agendamento ele quer cancelar (utilizar o id do agendamento).
    - O processo de cancelar agendamento é um processo automático, sendo necessário
apenas alterar o STATUS do horário na agenda. Pode-se ser utilizado uma
identificação para cada horário, por exemplo D – disponível e R - reservado.
    - O sistema deverá apresentar a mensagem de cancelamento. Ex: ‘O agendamento
(id:8521) está cancelado com sucesso!!!

- Cadastro de Serviço.
    - Nessa tela a clínica terá a opção cadastrar os serviços prestados e suas quantidades para cálculo do custo do serviço. As informações são:
        - Data
        - Descrição do Serviço
            - Clínica Geral: R$150,00
            - Clareamento: R$250,00
            - Tratamento de Canal: R$350,00
            - Implante Dentário R$500,00
        - O sistema deverá apresentar a mensagem de serviço realizado juntamente com o custo total do serviço. Ex: ‘O serviço referente ao agendamento (id:8521) foi realizado com sucesso!!! O valor total do serviço foi de R$xxx,xx’

- Relatórios.
    - Todas os relatórios devem conter um cabeçalho e ser apresentado de forma tabular. Nessa tela, o sistema deverá apresentar as seguintes opções:
        1. Relatório de todos os agendamentos.
        2. Relatório de agendamentos por pessoa (pesquisar por CPF).
        3. Relatório de receita total por mês.
        4. Relatório serviço prestado por pessoa (pesquisar por CPF).

Informações gerais para o desenvolvimento:
    - A linguagem para desenvolvimento deverá ser a linguagem Python.
    - Equipes de no máximo 3 pessoas.
    - Os desenvolvedores deverão utilizar de funções para cada tarefa. Exemplo:
    func_cadastro_cliente, func_agend_cliente, func_relatorio ...
    - Os desenvolvedores deverão utilizar de controle de fluxo para desenvolver o sistema, usar FOR ou WHILE, IF e ELIF.
    - Os desenvolvedores deverão utilizar de lista ou dict para armazenar as informações, ex lista_agendamentos = (), dic_agendamentos = {}.
    - Não é obrigatório, mas será considerado como um plus:
    - Salvar as informações em um arquivo .txt ou algum tipo de banco de dados.
    - Criar algum tipo de interface utilizando ferramentas como PyQt.
