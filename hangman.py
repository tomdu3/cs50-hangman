import pprint
hangman = {}
first = []
with open('hangman.txt') as f:
    first = f.read().split('()\n')

for index, value in enumerate(first):
    hangman[len(first)-index-1] = value


pprint.pprint(hangman)
for value in hangman.values():
    print(value)
