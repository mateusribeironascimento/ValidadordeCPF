import re

print('=' * 32)
print(f'{"VALIDADOR DE CPF":^32}')
print('=' * 32)
cpf = ''
while True:
    cpf = input('Digite o CPF: ').strip()
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) > 11 or len(cpf) < 11:
        print('CPF inválido')
        print('-' * 32)
    elif cpf[0] * len(cpf) == cpf:
        print('CPF inválido')
        print('-' * 32)
    else:
        break

inicial = 10
soma = 0
for i in range(0, 9):
    soma += (int(cpf[i]) * inicial)
    inicial -= 1
soma *= 10
resto = soma % 11
digito_1 = 0 if resto > 9 else resto

inicial_2 = 11
soma_2 = 0
for i in range(0, 10):
    soma_2 += (int(cpf[i]) * inicial_2)
    inicial_2 -= 1
soma_2 *= 10
resto_2 = soma_2 % 11
digito_2 = 0 if resto_2 > 9 else resto_2

cpf_2 = cpf[0:9] + str(digito_1) + str(digito_2)

if cpf == cpf_2:
    print('-' * 32)
    print('Esse CPF digitado é válido')
else:
    print('-' * 32)
    print('Esse CPF digitado é inválido')