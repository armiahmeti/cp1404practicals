
"""
CP1404/CP5632 Practical - Enhanced Solution
Testing code using assert and doctest
"""

import doctest

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a period.
    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('this is cool')
    'This is cool.'
    """
    sentence = phrase.capitalize()
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence

def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("hi", 2) == "hi hi"
    assert is_long_word("Python", 6) is True
    assert is_long_word("short", 7) is False
    assert phrase_to_sentence("example") == "Example."

run_tests()
doctest.testmod()
