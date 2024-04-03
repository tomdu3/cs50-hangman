# Hangman Game

#### Video Demo: [https://youtu.be/9O5YFeWEpbk](https://youtu.be/9O5YFeWEpbk)

#### Description:
This project is a simple implementation of the classic game "Hangman" in Python. The game is designed to be run in the command line and offers a fun and interactive way to guess words letter by letter.

In this version of Hangman, a player tries to guess a word by suggesting letters within a certain number of guesses. Each wrong guess brings the hangman closer to being fully drawn and the game closer to an end. The game uses a list of words imported from a file and ASCII art to visually represent the hangman's stages.

### How to Play
1. The game selects a random word from a predefined list of words.
2. The player guesses one letter at a time.
3. If the guessed letter is in the word, the game reveals its position(s) in the word.
4. If the guessed letter is not in the word, one life is deducted and part of the hangman is drawn.
5. The game continues until either the player guesses the word correctly or runs out of lives.

### Features
- Random word selection from an external file.
- Dynamic ASCII art to represent the hangman.
- Input validation to ensure that only single letters are accepted as guesses.
- Case-insensitive guessing.

### Requirements
- Python 3.x
- External files: `words.txt` for the word list and `hangman.txt` for the ASCII art stages.

### Setup and Running
1. Ensure Python 3.x is installed on your system.
2. Clone this repository or download the source code.
3. Place `words.txt` and `hangman.txt` in the same directory as `project.py`.
4. Run the game using the command `python project.py`.

### Project Structure
- `project.py`: Contains the main game logic and functions.
- `words.txt`: A text file containing possible words to guess.
- `hangman.txt`: A text file containing the ASCII art for the hangman stages.
- `lose.txt`: A text file containing the ASCII art for the game over - lose.
- `win.txt`: A text file containing the ASCII art for the game over - win.
- `test_project.py`: Contains tests for key functions of the game, executable with pytest.


### Testing

This project includes unit tests for the `words_import`, `hangman_import`, and `print_hangman_word` functions, ensuring that key components of the game behave as expected under various conditions. Here's a brief overview of what each test verifies:

- `test_words_import`: Checks if the `words_import` function successfully reads from the `words.txt` file, returns a list, and ensures that the list contains strings representing words. This test ensures that the game has a valid word list to choose from.

- `test_hangman_import`: Ensures that the `hangman_import` function properly loads the ASCII art representations of the hangman's stages from `hangman.txt` into a dictionary, validating the structure and content of this dictionary. This is crucial for visually representing the game's progress.

- `test_print_hangman_word`: Verifies the `print_hangman_word` function's ability to correctly print the current state of the word being guessed, with letters either revealed or represented as underscores based on the player's guesses. This test captures and examines the function's output to ensure it matches the expected format.

To run these tests, ensure you have `pytest` installed in your environment:

```sh
pip install pytest
```

Then, execute the following command in the terminal in your project's root directory:

```sh
pytest test_project.py
```

Pytest will automatically discover and run the tests defined in test_project.py, providing feedback on their success or failure. This testing step is crucial for maintaining the game's functionality and making it robust against errors.


### Author

- Name: Tomislav Dukez
- GitHub: tomdu3
- EdX: tomdu3
- Location: London, UK
- Date: 3 April 2024

#### Acknowledgments
- ASCII Art for hangman stages inspired by [Invent with Python](https://inventwithpython.com/bigbookpython/project34.html)
- Word list sourced from [Hangman Words](https://www.hangmanwords.com/words)

Enjoy playing Hangman and feel free to contribute or suggest improvements!
