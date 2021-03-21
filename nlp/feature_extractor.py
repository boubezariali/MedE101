import re

import glog
import stanza

from file_utils.array_io_utils import read_array
from preprocessing.string_cleaning_utils import (get_punctuation,
                                                 get_stopwords,
                                                 remove_stopchars,
                                                 remove_stopstrings, stem)


class FeatureExtractor:

    CLINICAL_FEATURES_FILE = 'main_data/clinical_keywords.csv'

    def __init__(self, features=CLINICAL_FEATURES_FILE):
        self.contents_ = []
        array = read_array(features)
        self.stopwords_ = get_stopwords()
        self.punctuation_ = get_punctuation()
        glog.info("Read data complete.")
        for elem in array:
            words = elem[0].split(" ")
            words = remove_stopstrings(words, self.stopwords_)
            words = [remove_stopchars(word, self.punctuation_) for word in words]
            words = [stem(word) for word in words]
            self.contents_.append(set(words))
        glog.info("Load data complete.")

    def get_mimic_features(self, text):
        stanza.download('en', package='mimic', processors={'ner': 'i2b2'})
        nlp = stanza.Pipeline('en', package='mimic', processors={'ner': 'i2b2'})
        doc = nlp(text)
        result = []

        # Loop through all the entities found in the text.
        for ent in doc.entities:
            # Construct a set of cleaned words from entity.
            words = ent.text.split(' ')
            words = remove_stopstrings(words, self.stopwords_)
            words = [remove_stopchars(word, self.punctuation_) for word in words]
            words = [stem(word) for word in words]
            words_set = set(words)
            # Loop through all our stored clinical features.
            for feature in self.contents_:
                # Check that all the words in the feature are in the set.
                valid_feature = True
                for word in feature:
                    if word not in words_set:
                        valid_feature = False
                # If all words are found then this is likley to be a valid feature.
                if valid_feature and len(feature) > 0:
                    result.append(feature)
        return result

    def get_windowed_features(self, text):
        stanza.download('en', processors='tokenize')
        nlp = stanza.Pipeline('en', processors='tokenize')
        doc = nlp(text)
        result = []
        # Get all sentences in the input text.
        sentences = [sentence.text for sentence in doc.sentences]

        for sentence in sentences:
            # Split the sentence into its clauses seperated by , or ;
            clauses = re.split(';|,', sentence)
            for clause in clauses:
                # Clean up each clause.
                clause = clause.split(' ')
                clause = remove_stopstrings(clause, self.stopwords_)
                clause = [remove_stopchars(word, self.punctuation_) for word in clause]
                clause = [stem(word) for word in clause]
                clause_set = set(clause)
                # Loop through all our stored features.
                for feature in self.contents_:
                    valid_feature = True
                    for word in feature:
                        if word not in clause_set:
                            valid_feature = False
                    # If all words are found then this is likley to be a valid feature.
                    if valid_feature and len(feature) > 0:
                        result.append(feature)
        return result
