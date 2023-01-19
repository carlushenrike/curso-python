"""
Aula 08 - While/else
Acumuladores (soma)
contadores
?
"""
counter = 1
sum = 1
while counter <= 10:
    print(counter, sum)
    # if counter > 5: # ignore else
    #     break
    sum += counter
    counter += 1
else:
    print('else')
print('else')
