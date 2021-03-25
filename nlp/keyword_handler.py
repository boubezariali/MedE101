""" Class definition for KeywordHandler.
"""
import glog

from file_utils.array_io_utils import read_array
from nlp.stanza_utils import get_stanza_model
from preprocessing.string_cleaning_utils import (get_punctuation,
                                                 get_stopwords,
                                                 remove_stopchars,
                                                 remove_stopstrings, stem)


class KeywordHandler:
    """ Handler class for all clinical features. Instances of this class
    are used by FeatureExtractors to maintain a consistent set 
    punctuation and stopwords to clean off of.
    """

    CLINICAL_FEATURES_FILE = 'data/main_data/clinical_keywords.csv'

    def __init__(self, features=CLINICAL_FEATURES_FILE):
        self._contents = []
        array = read_array(features)
        self._stopwords = get_stopwords()
        self._punctuation = get_punctuation()
        glog.info("Read data complete.")
        for elem in array:
            words = elem[0].split(" ")
            words = remove_stopstrings(words, self._stopwords)
            words = [remove_stopchars(word, self._punctuation) for word in words]
            words = [stem(word) for word in words]
            self._contents.append(set(words))
        glog.info("Load data complete.")

    @property
    def keywords(self):
        return self._contents

    @property
    def stopwords(self):
        return self._stopwords

    @property
    def punctuation(self):
        return self._punctuation
