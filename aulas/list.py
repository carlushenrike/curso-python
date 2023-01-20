"""
# Aula 11 - Listas []
append, clear, pop, del, clear, extend, +
min, max
range
"""
list = [1, 2, 3, 4, 'Vada', True, 23.400000, -2323]

#        0    1    2    3    4
list = ['A', 'B', 'C', 'D', 'E']
#     -  5    4    3    2    1

print(list)
print(list[2])
print(list[-1])

list[1] = 'Ophelia'
print(list)

print(list[1:3])
print(list[::2])
print(list[::-1])  # inverting

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
listsum = list1 + list2
print(list1)
print(list2)
print(listsum)

list1.extend(list2)
print(list1)
print(list2)
list1.extend('a')
print(list1)
list1.append('b')
print(list1)
list1.insert(2, 'c')  # (position, character)
print(list1)
list1.pop()
print(list1)
del[list1[2:5]]
print(list1)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(list))
print(min(list))

list = range(0, 10)
print(list)

soma = 0
for n in list:
    print(f'{soma} + {n} = {soma+n}')
    soma += n
print('list sum:', soma)

list = ['Jenna', 23.3, -4, True]
for n in list:
    print(f'{n} type is: {type(n)}')


secretword = 'pizza'
while True:
    letter = input('type a letter or "ok" for reply: ').lower()
    if len(letter) > 1 and letter != 'ok':
        print('type only one letter')
        continue
    elif letter == 'ok':
        wordinp = input('enter the secret word: ')
        if wordinp == secretword:
            print('Correct!')
            break
        else:
            print('wrong')
            while True:
                tryinp = input('try again?[y/n] ').lower()
                if tryinp != 'y' or tryinp != 'n':
                    break
                else:
                    print('type "y" or "n"!')
            if tryinp == 'y':
                continue
            elif tryinp == 'n':
                break
            else:
                print('whatever')
    if letter in secretword:
        for character in secretword:
            if character == letter:
                print(character, end='')
            else:
                print('*', end='')
        print()
    else:
        print('letter does not exist')
