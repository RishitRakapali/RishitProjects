 # This is a guess the number game.
import random

guessesTaken = 0

print('What is the range of numbers you want to guess between?')
lowestValue = input('Lowest Value -- ')
highestValue = input('Highest Value -- ')

numberOfGuesses = input('How many guesses would you like to have?')

number = random.randint(int(lowestValue), int(highestValue))

while guessesTaken < int(numberOfGuesses):
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)