"""
# Aula 15 - Ternary Operator
"""

loggeduser = False
if loggeduser:
    msg = 'Logged'
else:
    msg = 'need to login'
print(msg)

msg = 'Logged user' if loggeduser else 'need to login'
print(msg)

age = int(input('age: '))
olderage = True if age >= 18 else False
print(olderage)

olderage = age >= 18
msg = 'can acess' if olderage else 'can not acess'
print(msg)
