import nltk

STOP_WORDS_FILE = 'preprocessing/stopwords.txt'
PUNCTUATION_FILE = 'preprocessing/punctuation.txt'

def word_tokenize(string): 
    return nltk.tokenize.word_tokenize(string)

def remove_stopstrings(strings, stopstrings): 
    return [s for s in strings if s not in stopstrings]

def get_stopwords():
    with open(STOP_WORDS_FILE, "r") as f:
        words = f.read().split("@@")
    return set(words)

def get_punctuation(): 
    with open(PUNCTUATION_FILE, "r") as f:
        punc = f.read().split("@@")
    return set(punc)

def add_word(path, word): 
    with open(path, "w") as f: 
        f.write(word + "@@")
 
