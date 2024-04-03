import pytest
from project import words_import, hangman_import, print_hangman_word
import sys
from io import StringIO

# Test for words_import function
def test_words_import():
    words = words_import('words.txt')  # words.txt has to exist
    assert isinstance(words, list), "The function should return a list"
    assert len(words) > 0, "The list should not be empty"
    assert all(isinstance(word, str) for word in words), "All items in the list should be strings"

# Test for hangman_import function
def test_hangman_import():
    hangman = hangman_import()
    assert isinstance(hangman, dict), "The function should return a dictionary"
    assert all(isinstance(key, int) for key in hangman.keys()), "All keys should be integers"
    assert all(isinstance(value, str) for value in hangman.values()), "All values should be strings"
    assert len(hangman) > 0, "The dictionary should not be empty"

# Test for print_hangman_word function
def test_print_hangman_word():
    word = "python"
    letters = ['p', 't', 'o']
    # Capture the output
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    print_hangman_word(word, letters)
    sys.stdout = sys.__stdout__  # Reset redirect
    assert capturedOutput.getvalue().strip() == 'p_t_o_', "The function should print the word with underscores for unguessed letters"