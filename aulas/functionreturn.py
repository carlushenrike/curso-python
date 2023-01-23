"""
Aula 16(2) - Funções (def)
- return
"""


def function(variable):
    print(variable)


variable = function('hi')
print(variable)
if variable:
    print('ok')
else:
    print('none')


def function(variable):
    return variable
    print('this will not run')


variable = function('hi')
print(variable)
if variable:
    print('ok')
else:
    print('none')


def division(n1, n2):
    if n2 > 0:
        return n1 / n2


def division(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


result = division(8, 0)
if result:
    print(result)
else:
    print('division error')


def dumb():
    return 1


print(dumb(), type(dumb()))


def dumb():
    return [1, 2, 3, 4, 5]


print(dumb(), type(dumb()))


def dumb():
    return


print(dumb(), type(dumb()))


def dumb():
    return True


print(dumb(), type(dumb()))


def a(v):
    print(v)


def dumb():
    return a


variable = dumb()('aaaaaaaaaa')
print(type(a))
variable = dumb()
if variable == a:
    print('what')
else:
    print('whatever')

print(type(variable))
variable('became a function')


def dumb():
    return ('malt', 'dofia')


variable = dumb()
print(variable, type(variable))
