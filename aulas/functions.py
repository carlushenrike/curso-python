"""
Aula 16 - Funções python (def)
"""
print('hi my death trap')


def function():
    print('hi my death trap')


function()
function()
function()
function()


def function(msg):
    print(msg)


function('Hi')


def greeting(msg='hi', name='user'):
    name = name.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, name)


greeting()
greeting('welcome', 'Tyler')
greeting('hi', 'Emma')
greeting('hello', 'Gomez')
greeting(name='ashley', msg='hi')


def greeting(msg='hi', name='user'):
    name = name.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {name}'


variable = greeting('hi', 'Emma')
print(variable)
