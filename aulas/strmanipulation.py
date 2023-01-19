"""
# Aula 06 - Manipulando Strings
- [inicio:fim:passo]
- Funções: len, abs, type, print, etc.
"""
# positive   [01234567]
text = 'whatever'
# negative  -[87654321]
print(text[2])
print(text[:4])
print(text[4:8])
print(text[4:])
print(text[1:3:8])

url = 'www.google.com.br/'
print(url[0:17])
print(url[:-1])

print(len(text))

for letter in text:
    print(letter)
