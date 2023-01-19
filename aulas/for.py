"""
# Aula 10 - loop For in
- Iterar str com for
- Função range(start=0, stop, step=1)

"""
str = 'zunzun'
for letter in str:
    print(letter)

for n, letter in enumerate(str):
    print(n, letter)

for number in range(10): # (0, 10, 1)
    print(number)

for number in range(5, 15, 2):
    print(number)

for number in range(20, 10, -1):
    print(number)

newstr = ''
for letter in str:
    if letter == 'u':
        newstr += letter.upper()
    elif letter == 'n':
        newstr += letter.upper()
    else:
        newstr += letter
print(newstr)
