""" Utility files for cleaning strings. 
"""
import nltk
import string

from file_utils.array_io_utils import lined_file_to_array

STOPWORDS_FILE = "preprocessing/stopwords.txt"
PUNCTUATION_FILE = "preprocessing/punctuation.txt"


def word_tokenize(string):
    """Tokenize a string into individual words.
    Args:
        param string: str
    Returns:
        list of strings
    """
    return nltk.tokenize.word_tokenize(string)


def remove_stopstrings(strings, stopstrings):
    """Removes a list of stopstrings from a list of strings.
    Args:
        param strings: list of input strings to clean
        param stopstrings: list of stopstrings to check against.
    Returns:
        list of strings
    """
    return [s for s in strings if s not in stopstrings]

def remove_stopchars(strings, stopchars):
    """Removes a list of characters from the words, modifying the words
    themselves. 
    Args:
        param strings: list of input strings to clean.
        param stopchars: list of strings to check for in the words.
    Returns:
        list of strings
    """
    stopchars_str = ''.join(stopchars)
    return [s.translate(str.maketrans('', '', stopchars_str)) for s in strings]

def get_stopwords():
    """Get the global list of english stopwords from the predetermined file."""
    array = lined_file_to_array(STOPWORDS_FILE)
    return set(array)


def get_punctuation():
    """Get the global list of punctuation from the predetermined file."""
    array = lined_file_to_array(PUNCTUATION_FILE)
    return set(array)
