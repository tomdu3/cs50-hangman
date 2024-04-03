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

print(WORDS)