from file_utils.array_io_utils import read_array
from preprocessing.string_cleaning_utils import get_stopwords, get_punctuation, remove_stopstrings

import glog
import pandas as pd

class FuzzyFinder: 
    CLINICAL_FEATURES_FILE = 'main_data/clinical_keywords.csv'
    def __init__(self, features=CLINICAL_FEATURES_FILE):
        self.contents = [] 
        array = read_array(features)
        stopwords = get_stopwords()
        punctuation = get_punctuation()

        glog.info("Read data complete.")

        for elem in array:
            words = elem[0].split(" ")  
            words = remove_stopstrings(words, stopwords)
            words = remove_stopstrings(words, punctuation)
            self.contents.append(set(words))

        glog.info("Load data complete.")

        print(self.contents)
        
