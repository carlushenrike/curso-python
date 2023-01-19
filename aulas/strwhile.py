"""
# Aula 09 - Iterando strings with while

"""

str = 'i have a hard time moving forward'
counter = 0
while counter < len(str):
    print(str[counter])
    counter += 1

counter = 0
newstr = ''
while counter < len(str):
    if str[counter] == 'a':
        newstr += str[counter].upper()
    else:
        newstr += str[counter]
    counter += 1
print(newstr)
print(str.count('a'))

counter = 0
cb = 0
letterb = ''
while counter < len(str):
    # print(str[counter], str.count(str[counter]))
    if str[counter] != ' ':  # voidspace
        if str.count(str[counter]) > cb:
            cb = str.count(str[counter])
            letterb = str[counter]
    counter += 1
print(letterb, cb)
