from random import *

print('-'*10+'GUESSING GAME'+'-'*10)
print('Number that you will guess is between 1 to 100')
print('Lets start to guess')


countGuessed = 0
randomNumber = randint(1,101)
print('randomNumber: %d'%randomNumber)
guessedDiff = 0
firstGuess = True

while True:
    guessingNumber = int(input('Guess [1-100]: '))
    countGuessed +=1
    tempGuessingDiff = abs(guessingNumber-randomNumber)

    if guessingNumber > 100 or guessingNumber < 1:
        print('OUT OF BOUNDS')
        continue
    elif tempGuessingDiff==0:
        print('You won, Winner Chicken..! %d try'%countGuessed)
        break
    elif firstGuess and tempGuessingDiff>10:
        firstGuess= False
        print('COLD')
    elif firstGuess and tempGuessingDiff<10:
        firstGuess= False
        print('WARM')
    elif tempGuessingDiff>guessedDiff:
        print('COLDER')
    elif tempGuessingDiff<guessedDiff:
        print('WARMER')
    else:
        print('Try different number')

    guessedDiff=tempGuessingDiff
