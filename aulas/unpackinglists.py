"""
Aula 14 - Desempacotando listas
"""

list = ['Jenna', 'Mia', 'Vada']
v1, v2, v3 = list
print(v2)
list = ['Jenna', 'Mia', 'Vada', 1, 2, 3, 4, 5]
v1, v2 , *list2, last = list
print(v1, v2, list2)
print(list2)
print(last)
