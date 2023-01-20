"""
Aula 13 - 
. split | str
. join | str
. enumerate | list # tuple
"""

str = "you need sleep to have nightmares"
list = str.split(' ')
list2 = str.split('e')
print(list)
print(list2)
for value in list:
    print(f'{value} : {list.count(value)}')

str = 'rope shovel hole'
list = str.split(' ')
print(list)
str2 = ', '.join(list)
print(str2)

for index, value in enumerate(list):  # enumerate: tuple
    print(index, value, list[index])

list = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(list)
for value in list:
    print(value)
for value in list:
    print(value[0], value[1])

list = [   # enumerate ?list?
    [0, 'rope'],
    [1, 'shovel'],
    [2, 'hole']
]
for index, value in list:
    print(index, value)

list = ['rope', 'shovel', 'hole']
value1, value2, value3 = list
print(value1)
print(value2)
print(value3)
