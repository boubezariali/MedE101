""" Class definition for ClauseFeatureExtractor.
"""
import re
from file_utils.array_io_utils import read_array
from nlp.stanza_utils import get_stanza_model
from preprocessing.string_cleaning_utils import (get_punctuation,
                                                 get_stopwords,
                                                 remove_stopchars,
                                                 remove_stopstrings, stem)
from nlp.feature_extractors.feature_extractor import FeatureExtractor

class ClauseFeatureExtractor(FeatureExtractor):
    """Extracts keywords residing in the same clause within a sentence.
    Does not specialize or do well with lists.
    """

    def get_features(self, text):
        nlp = get_stanza_model(processors='tokenize', download=False)
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
                clause = remove_stopstrings(clause, self._keyword_handler.stopwords)
                clause = [remove_stopchars(word, self._keyword_handler.punctuation) for word in clause]
                clause = [stem(word) for word in clause]
                clause_set = set(clause)
                # Loop through all our stored features.
                for feature in self._keyword_handler.keywords:
                    valid_feature = True
                    for word in feature:
                        if word not in clause_set:
                            valid_feature = False
                    # If all words are found then this is likley to be a valid feature.
                    if valid_feature and len(feature) > 0:
                        result.append(' '.join(feature))
        return result
