"""
# Aula 12 - For / else

"""

""" 
variable = ['Emma', 'Jenna', 'Vada']
for value in variable:
    if value.lower().startswith('j'):
        print('starts with "J":', value)
    else:
        print('not start with "J"', value)

startj = False
for value in variable:
    if value.startswith('J'):
        startj = True
if startj:
    print('there is word with "j"')
else:
    print('there is no word with "j"')
 """
variable = ['Emma', 'Jenna', 'Vada']
for value in variable:
    print(value)
    if value.lower().startswith("j"):
        break
else:
    print('there is no word with "j"')
