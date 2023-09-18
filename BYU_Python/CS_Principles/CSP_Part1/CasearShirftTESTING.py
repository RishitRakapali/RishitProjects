import random
plainText = 'a b cd'

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



key = random.randint(2, 100)

cipheredText = []

'''
for word in plainText:
    for letter in word:
        index = alphabet.index(letter)
        cipheredText.append(alphabet[ (index + 2) % 26])
'''


for letter in plainText:
    if letter != ' ':
        index = alphabet.index(letter)
        cipheredText.append(alphabet[ (index + 2) % 26])
    else:
        cipheredText.append(letter)

print(plainText)
print(cipheredText)

for character in cipheredText:
    print(character, end = '')


