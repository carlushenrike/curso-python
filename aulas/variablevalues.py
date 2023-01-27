def p(): return print()


x = 10  # 'hi'
y = 'hi'  # 10

z = x
x = y
y = z

print(f'X = {x}\nY = {y}')
p()
x = 10
y = 'hi'

x, y = y, x
print(f'X = {x}\nY = {y}')
p()
x = 10
y = 'hi'
z = 'cool'
x, y, z = z, x, y
print(f'X = {x}\nY = {y}\nZ = {z}')
