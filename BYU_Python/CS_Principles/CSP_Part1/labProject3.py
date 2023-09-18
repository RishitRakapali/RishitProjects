import random
import time

def playerName():
    print('Enter your player\'s name')
    name = input()
    return name

def displayIntro():
    print(name + ' is in a land full of dragons. In front of')
    print(name + ' are three caves. In one cave, the dragon is friendly')
    print('and will share his treasure with ' + name + '. Another dragon')
    print('is greedy and hungry and will eat ' + name + ' on sight.')
    print('The last dragon is a rare dragon, which will reward you with a')
    print('present if ' + name + ' encounters it.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave does ' + name + ' go into? (1, 2, or 3)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 3)

    if chosenCave == str(friendlyCave):
         print('Gives ' + name + ' his treasure!')
    elif chosenCave == str(friendlyCave - 1):
         print('Gives ' + name + ' a present!')
    else:
         print('Gobbles ' + name + ' down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    name = playerName()

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()