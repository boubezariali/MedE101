from file_utils.array_io_utils import read_array
from preprocessing.string_cleaning_utils import get_stopwords, get_punctuation, remove_stopstrings, remove_stopchars, stem
from fuzzyset import FuzzySet

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
            words = [remove_stopchars(word, punctuation) for word in words]
            words = [stem(word) for word in words]
            self.contents.append(set(words))
        glog.info("Load data complete.")

    def get_features_from_sentence(self, sentence):
        sentence = [stem(word) for word in sentence]
        print(sentence)
        fuzzy_set = FuzzySet(sentence)
        result = []
        for elem in self.contents:
            valid_feature = True
            for word in elem:
                score = fuzzy_set.get(word)
                if score is None or score[0][0] < 0.75:
                    valid_feature = False
                    break
            if valid_feature:
                result.append(elem)
        return result
                
                

                
        


        

