"""
# Aula 17 - Expressões Lambda(Funções anônimas)
"""


def func(value, value2):
    return value * value2


var = func(2, 2)
print(var)


var = lambda x, y: x * y
print(var(2, 4))

list = [
    ['P1', 2],
    ['P2', 9],
    ['P3', 5],
    ['P4', 34],
    ['P5', 10]
]
list.sort(key=lambda i: i[1], reverse=True)
print(list)
