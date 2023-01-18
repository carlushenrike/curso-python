maioridade = 30
menoridade = 20
idade = int(input('Idade: '))
if idade > maioridade:
    print('Não pode pagar empréstimo')
elif idade < menoridade:
    print('Não pode pagar empréstimo')
else:
    print('Pode pagar empréstimo')

if idade > maioridade or idade < menoridade:
    print('Não pode pagar empréstimo')

"""
and, or, not
not in, in
"""

nome = "Carlos Henrique"
if "Car" in nome:
    print('existe')
else:
    print('não existe')

a = 0
if not a:
    print('Preencha valor de A')
else:
    print('a')

b = 2
if not b < a:
    print('B maior que A')
else:
    print('A maior que B')


usuario = input('Usuário:')
senha = input('Senha:')
print(type(senha))
usuarioms = 'Carlos'
senhams = "bD'h2x54"

if usuario == usuarioms and senha == senhams:
    print('Connected')
else:
    print('Invalid Error')
