import random

'''
The Caesar-shifter program take a string as an input to encrypt into a new string which isn't readable. It also outputs
a key which the user then can use to decrypt the string back into its original form. This is also commonly known as 
the Caeser Cipher or the Shift Cipher.
'''

'''
This function encrypts the given plainText by using the given key to shift each letter in the text that many 
spaces forward in the alphabet.
'''
def encryptionMachine(plainText, alphabet, key):
    cipheredText = []

    for letter in plainText:
        if letter != ' ':
            index = alphabet.index(letter)
            #Formula for shifting letters in a caesar cipher
            cipheredText.append(alphabet[ (index + int(key)) % 94])
        else:
            cipheredText.append(letter)

    return cipheredText

#Takes the encrypted text and key to revert it back to its original form
def decryptionMachine(cipherText, alphabet, key):
    decryptedText = []

    for letter in cipherText:
        if letter != ' ':
            index = alphabet.index(letter)
            # Formula for shifting letters back into plain text in a caesar cipher
            decryptedText.append(alphabet[(index - int(key)) % 94])
        else:
            decryptedText.append(letter)

    return decryptedText

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', '`', '\'', '\"', ':', ';', '<', '>', ',', '.', '?',
            '/', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\']
print('''
                 _________________________________ 
                |  _____________________________  |
                | | C A E S A R - S H I F T E R | |
                | |_____________________________| |
                |_________________________________|
''')

print('* Welcome to Caesar Shifter! Here you can encrypt or decrypt your text with ease! *\n')

#Makes sure the user is either encrypting or decrypting
choice = input('Would you like to encrypt or decrypt your text: ').lower()
while choice != 'encrypt' and choice != 'decrypt':
    print('That is not a valid operation. You can either encrypt or decrypt your text.')
    choice = input('Would you like to encrypt or decrpyt: ').lower()
print()

#Here, the program check if the user is encrypting or decrypting. I am still working on the decrypting function.
if choice == 'encrypt':
    #Takes text from the user to encrypt.
    encryptionKey = random.randint(2, 100)
    plainText = input('Enter text: ')
    encryptedText = encryptionMachine(plainText, alphabet, encryptionKey)

    #Prints the final encrypted message and key to the user
    print('Your encrypted text is:')
    for character in encryptedText:
        print(character, end = '')
    print()
    print('The KEY to decrpyt this text is: ' + str(encryptionKey))
elif choice == 'decrypt':
    #Takes the ciphered text and key from the user to decrypt
    cipherText = input('Enter encrypted text: ')
    decryptionKey = input('Enter key: ')
    decryptedText = decryptionMachine(cipherText, alphabet, decryptionKey)

    #Prints the final decrypted message and key to the user
    print('Your decrypted text is:')
    for character in decryptedText:
        print(character, end = '')
    print()


