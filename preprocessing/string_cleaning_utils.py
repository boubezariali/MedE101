""" Utility files for cleaning strings. 
"""
import string

import contractions
import nltk
import spacy
import unidecode
from bs4 import BeautifulSoup
from nltk.stem.snowball import SnowballStemmer

from file_utils.array_io_utils import lined_file_to_array
from file_utils.runfile_utils import runfile_location

STOPWORDS_FILE = "preprocessing/stopwords.txt"
PUNCTUATION_FILE = "preprocessing/punctuation.txt"


def get_stopwords():
    """Get the global list of english stopwords from the predetermined file."""
    array = lined_file_to_array(runfile_location(STOPWORDS_FILE))
    return set(array)


def get_punctuation():
    """Get the global list of punctuation from the predetermined file."""
    array = lined_file_to_array(runfile_location(PUNCTUATION_FILE))
    return set(array)


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


def remove_stopchars(string, stopchars):
    """Removes a list of characters from the words, modifying the words
    themselves. 
    Args:
        param strings: a string to clean.
        param stopchars: list of strings to check for in the words.
    Returns:
        the cleaned string
    """
    stopchars_str = ''.join(stopchars)
    return string.translate(str.maketrans('', '', stopchars_str))


def stem(string):
    """Gets the stem or base of an english word. If the word is not
    english or invalid, the input string will be returned.
    Args:
        string: string to process.
    Returns:
        the stem of the string.
    """
    stemmer = SnowballStemmer("english")
    return stemmer.stem(string)


def strip_html_tags(text):
    """remove html tags from text"""
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text(separator=" ")
    return stripped_text


def remove_accented_chars(text):
    """remove accented characters from text, e.g. café"""
    text = unidecode.unidecode(text)
    return text


def expand_contractions(text):
    """expand shortened words, e.g. don't to do not"""
    text = contractions.fix(text)
    return text
