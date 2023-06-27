import random

print('=' * 20)
print(f'{"GERADOR DE CPF":^20}')
print('=' * 20)

cpf = ''
for l in range(11):
    cpf += str(random.randint(0, 9))

inicial = 10
soma = 0
for i in range(0, 9):
    soma += (int(cpf[i]) * inicial)
    inicial -= 1
soma *= 10
resto = soma % 11
digito_1 = 0 if resto > 9 else resto

cpf = cpf[0:9] + str(digito_1)

inicial_2 = 11
soma_2 = 0
for i in range(0, 10):
    soma_2 += (int(cpf[i]) * inicial_2)
    inicial_2 -= 1
soma_2 *= 10
resto_2 = soma_2 % 11
digito_2 = 0 if resto_2 > 9 else resto_2

cpf_2 = cpf[0:9] + str(digito_1) + str(digito_2)

print(cpf_2)
