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
