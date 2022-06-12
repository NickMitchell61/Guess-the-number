"""import for random number in game"""
import random
import time


def anytext(text):
    '''Makes all game text typed'''
    for i in str(text):
        time.sleep(0)
        print(i, end='', flush=True)


anytext('\nIn this game try to guess the number between 1 to max*')

MAX_NUMBER = 0

while MAX_NUMBER == 0:
    try:
        anytext(MAX_NUMBER := int(input('\nEnter the max number or press the Enter to max is 50: ') or '50'))
    except ValueError as ve:
        anytext('\nError. You can enter only the number. Try again..')

RAND = random.randint(1, MAX_NUMBER)

TRIES = 6

anytext(f'\nOK, let\'s play. \nYou have an {TRIES} tries')
anytext('\nWhat the number did I guess?: ')

while TRIES > 0:
    try:
        answer = int(input())

        TRIES -= 1

        if answer > RAND:
            anytext('\nYour number is bigger then I guess number')
            anytext(f'\nYou have an {TRIES} tries')
            anytext('\nEnter the next number: ')
        elif answer < RAND:
            anytext('\nYour number is lower then I guess')
            anytext(f'\nYou have an {TRIES} tries')
            anytext('\nEnter the next number: ')
        else:
            anytext('\nYou WIN!')
            anytext(f'\nThe number what I guess is {RAND}')
            break
    except ValueError as ve:
        anytext('\nError. You can enter only the number. Try again..')
        anytext('\nEnter the number: ')
else:
    anytext('\nYou lose this game :(')
    anytext(f'\nThe number what I guess is {RAND}\n\n')
