secretword = 'wednesday'
# secretwordinp = ''
lettersinp = []
attempts = 3
while True:
    secretwordinp = ''
    letterinp = input('type a letter: ').lower()
    if len(letterinp) > 1:
        print('enter only one letter!')
        continue
    if letterinp in secretword:
        if letterinp in lettersinp:
            print('already typed', letterinp)
        else:
            lettersinp.append(letterinp)
    else:
        attempts -= 1
    for letter in secretword:
        if letter in lettersinp:
            secretwordinp += letter
        else:
            secretwordinp += '*'
    print(secretwordinp)
    print('Attempts:', attempts)
    if secretwordinp == secretword:
        print('game over')
        break
    elif attempts <= 0:
        print('you lost')
        break
