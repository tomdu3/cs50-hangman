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

def print_hangman_word(word, letters=[]):
    '''
    Prints a word letter by letter. If a letter in the word is
    not yet guessed, it prints an underscore character
    '''

    for letter in word:
        if letter in letters:
            print(letter, end='')
        else:
            print('_', end='')
    print()

def game_over(lives):

    if lives == 0:
        filename = 'lose.txt'
    else:
        filename = 'win.txt'

    with open(filename) as file:
        output = file.read()

    print(output)

def main():
    word = random.choice(WORDS)
    lives = 7
    letters_in_word = {letter for letter in word}
    correct_letters = []
    wrong_letters = []
    print_hangman_word(word, correct_letters)

    while lives > 0 and len(correct_letters) != len(letters_in_word):
        # verification of the user's input
        while True:
            guess_letter = input('guess a letter: ').lower().strip()
            if not guess_letter.isalpha():
                print('Invalid input! Only the letters are permitted!')
            elif len(guess_letter) != 1:
                print('Invalid input! The guess should be only one letter!')
            else:
                break

        # verification of the correct guess
        if guess_letter in correct_letters or guess_letter in wrong_letters:
            print("you've already guessed this letter")
        elif guess_letter not in letters_in_word:
            lives -= 1
            print(f'the letter {guess_letter} is not in the word! Lives: {lives}')
            print(HANGMAN[lives])
            wrong_letters.append(guess_letter)
            if lives == 0:
                break
        else:
            print(f'good one! the letter {guess_letter} is in the word!')
            correct_letters.append(guess_letter)
        print_hangman_word(word, correct_letters)

    game_over(lives)

if __name__ == '__main__':
    main()
