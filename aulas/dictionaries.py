"""
# Aula 20 - Dicionários
"""
import copy
def p(): return print()


dictionarie = {'key': 'key value'}
print(dictionarie)
dictionarie['new key'] = 'new key value'
print(dictionarie)
print(dictionarie['new key'])

dictionarie = dict(key1='key value', key2='key2 value')
print(dictionarie)

dictionarie = {'key': 'key value', 'key': 'key value', 'key': 'real key value'}
print(dictionarie)

dictionarie = {
    'str': 'value',
    321: 'other value',
    (1, 2, 3): 'tuple'
}
print(dictionarie)
print(dictionarie[(1, 2, 3)])
# dictionarie['keyname'] = 'valuekey'
if dictionarie.get('keyname') is not None:
    print(dictionarie.get('keyname'))
    print(dictionarie['keyname'])
else:
    print('none key')

print(dictionarie)
del dictionarie[321]
print(dictionarie)

print('str' in dictionarie)  # keys
print('str' in dictionarie.keys())
print('value' in dictionarie.values())
print(len(dictionarie))

p()
dictionarie = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4'
}
for data_key in dictionarie:
    print(data_key)
p()
for data_value in dictionarie.values():
    print(data_value)
p()
for data_key in dictionarie.items():  # tuples
    # print(key)
    print(data_key[0], data_key[1])
p()
for data_key, data_value in dictionarie.items():
    print(data_key, data_value)

p()
users = {
    'user1': {
        'name': 'Negan',
        'id': 3245
    },
    'user2': {
        'name': 'Eliza',
        'id': 6793
    }
}
print(users)
for users_key, users_value in users.items():
    print(users_key, end=':\n')
    # print(users_value)
    for data_key, data_value in users_value.items():
        print(data_key, data_value)

dictionarie = {1: 'a', 2: 'b', 3: 'c'}
dictionarie2 = dictionarie
print(dictionarie)
print(dictionarie2)
dictionarie2[1] = 'abab'
print(dictionarie)
print(dictionarie2)
print(dictionarie == dictionarie2)
dict1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['luiz', 'carlos']}
dict2 = dict1.copy()
dict2[1] = 'abab'
print(dict1)
print(dict2)
print(dict1 == dict2)
print(dict2['d'][0])
dict2 = copy.deepcopy(dict1)  # completely independent dictionaries

list = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
]
dictionarie = dict(list)
print(dictionarie)
print(dictionarie['c3'])
dictionarie.pop('c2')
print(dictionarie)
dictionarie.popitem()
print(dictionarie)

dict1 = {
    'c4': 2,
    'c5': 23
}
dict2 = {
    'c6': 2,
    'c7': 23
}
dict1.update(dict2)
print(dict1)
