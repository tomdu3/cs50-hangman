import random

def words_import(filename):
    '''
    Imports the words list from a file
    words taken from the website https://www.hangmanwords.com/words

    '''
    with open(filename, 'r') as file:
        words = file.readlines()
    return [word.strip() for word in words]


WORDS = words_import('words.txt')

def hangman_import():
    '''
    Imports hangman ASCI art that was taken from
    website https://inventwithpython.com/bigbookpython/project34.html
    '''

    hangman = {}
    with open('hangman.txt') as f:
        first = f.read().split('()\n')

    for index, value in enumerate(first):
        hangman[len(first)-index-1] = value

    return {key:value for key, value in hangman.items()}

HANGMAN = hangman_import()

for value in HANGMAN.values():
    print(value)