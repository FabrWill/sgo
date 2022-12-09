class Helpers:

    def validaCPF(cpf):
        cpf = cpf.replace('.', '').replace('-', '')

        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        if len(numbers) != 11 or len(set(numbers)) == 1:
            return True

        soma_produtos = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (soma_produtos * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return True

        soma_produtos = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (soma_produtos * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return True

        return False
    
    def response(status, message, contentName=False, content=False):
        response = {}
        response['status'] = status
        response['mensagem'] = message

        if (contentName and content):
            response[contentName] = content

        return response