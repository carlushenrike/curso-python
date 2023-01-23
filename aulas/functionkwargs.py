"""
# Aula 16(3) - Funções (def)
- *args and **kwargs
"""


def func(a1, a2, a3, name=None):
    print(a1, a2, a3, name)
    return a1, a2


func(2, 3, 4)
func(1, 2, 3, name='Carl')
var = func(1, 2, 3)
print(var)


def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    print(type(args))


func(1, 2, 3, 4, 5)


def func(*args):
    args = list(args)
    args[0] = 20
    print(args)
    print(type(args))
    for value in args:
        print(value)


func(1, 2, 3, 4, 5, 6, 7)


def func(*args):
    print(args)
    print(args[0])


list = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
func(list)  # tuple with list at index 2
func(list, 'a')

func(*list)
func(*list, *list2)


def func(*args, **kwargs):  # named arguments will go to kwargs, not args
    print(args)
    print(kwargs)
    print(type(kwargs))
    print(kwargs['name'], kwargs['id'])
    age = kwargs.get('age')
    if age:
        print(age)
    else:
        print('no age key')


func(*list, *list2, name='Xiaoya', id=12, age=18)
