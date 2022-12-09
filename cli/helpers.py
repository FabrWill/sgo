import datetime

def validaCPF(cpf):
    cpf = cpf.replace('.', '').replace('-', '')

    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    if len(numbers) != 11 or len(set(numbers)) == 1:
        print("CPF Inválido")
        return True

    soma_produtos = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (soma_produtos * 10 % 11) % 10
    if numbers[9] != expected_digit:
        print("CPF Inválido")
        return True

    soma_produtos = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (soma_produtos * 10 % 11) % 10
    if numbers[10] != expected_digit:
        print("CPF Inválido")
        return True

    return False

def validaData(data):
    try:
        datetime.datetime.strptime(data, '%Y-%m-%d')
        return False
    except ValueError:
        print("A data deve estar no formato AAAA-MM-DD")
        return True

def validaHora(hora):
    try:
        datetime.datetime.strptime(hora, '%H:%M')
        return False
    except ValueError:
        print("A hora deve estar no formato HH:MM")
        return True
