"""
Aula 18 - Tuplas
"""
tuple = (1, 2, 3, 4, 'a', 'im beautiful')
print(type(tuple))
print(tuple[3:])
print(tuple[5])
print(tuple)

tuple2 = 23, 6, 8, -2
tuplesum = tuple + tuple2
print(tuplesum)

v1, v2, v3, *_ = tuplesum
print(v1, v2, v3)

tuple = list(tuple)
tuple[1] = 'mutable'
print(tuple)
