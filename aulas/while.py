"""
# Aula 07 - Estrutura de repetição
- While
"""

# while True:  # infinite loop
#     name = input('name: ')
#     print('Hi', name)

n = 0
while n <= 10:
    if n == 3:  # skip 3
        n += 1
        continue
    print(n)
    n += 1
print('end')

n = 0
while n <= 10:
    if n == 3:
        break
    print(n)
    n += 1
print('end')

x = 0  # column
y = 0  # line
while x <= 5:
    y = 0
    while y <= 5:
        print(f'X = {x} | Y = {y}')
        y += 1
    x += 1
print('end')

# calculator
while True:
    n1 = input('number 1: ')
    n2 = input('number 2: ')
    if not n1.isnumeric() or not n2.isnumeric():
        print('just type numbers')
        continue
    n1 = int(n1)
    n2 = int(n2)
    operator = input('operator:')
    if operator == '+':
        print(n1 + n2)
    elif operator == '-':
        print(n1 - n2)
    elif operator == '/':
        print(n1 / n2)
    elif operator == '*':
        print(n1 * n2)
    else:
        print('Invalid Operator')
    while True:
        exit = input('Exit?[y/n] ').upper()
        if exit != 'Y' and exit != 'N':
            print('type y or n: ')
        else:
            break
    if exit == 'N':
        continue
    elif exit == 'Y':
        print('leaving...')
        break
