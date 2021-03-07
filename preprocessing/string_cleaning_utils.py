""" Utility files for cleaning strings. 
"""
import nltk

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
        returns: list of strings
    """
    return [s for s in strings if s not in stopstrings]


def get_stopwords():
    """Get the global list of english stopwords from the predetermined file."""
    array = lined_file_to_array(STOPWORDS_FILE)
    return set(array)


def get_punctuation():
    """Get the global list of punctuation from the predetermined file."""
    array = lined_file_to_array(PUNCTUATION_FILE)
    return set(array)
