""" Utility files for cleaning strings. 
"""
import nltk

from file_utils.delimeted_file import DelimetedFile

STOP_WORDS_FILE = 'preprocessing/stopwords.txt'
PUNCTUATION_FILE = 'preprocessing/punctuation.txt'

def word_tokenize(string): 
    """ Tokenize a string into individual words.
    :param string: str
    :returns: list of strings
    """
    return nltk.tokenize.word_tokenize(string)

def remove_stopstrings(strings, stopstrings): 
    """ Removes a list of stopstrings from a list of strings.
    :param strings: list of input strings to clean
    :param stopstrings: list of stopstrings to check against.
    :returns: list of strings
    """
    return [s for s in strings if s not in stopstrings]

def get_stopwords():
    """ Get the global list of english stopwords from the predetermined file.
    """
    df = DelimetedFile(STOP_WORDS_FILE) 
    return set(df.lst)

def get_punctuation(): 
    """ Get the global list of punctuation from the predetermined file.
    """
    df = DelimetedFile(PUNCTUATION_FILE)
    return set(df.lst)
 
