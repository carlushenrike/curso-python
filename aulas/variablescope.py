"""
Aula 16(4) - Variable Scope
Funções (def)
"""
variable = 'why'


def func():
    print(variable)


def func2():
    variable = 'ok'
    print(variable)


func()
func2()
print(variable)


def func3(arg=None):
    arg = arg.replace('y', 'at')
    return arg


variable2 = func3(arg=variable)
print(variable2)
