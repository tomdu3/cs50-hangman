import pytest
from project import words_import

# Test for words_import function
def test_words_import():
    words = words_import('words.txt')  # words.txt has to exist
    assert isinstance(words, list), "The function should return a list"
    assert len(words) > 0, "The list should not be empty"
    assert all(isinstance(word, str) for word in words), "All items in the list should be strings"