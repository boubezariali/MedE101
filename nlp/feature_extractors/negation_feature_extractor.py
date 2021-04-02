""" 
Class definition for NegationFeatureExtractor.
"""
from file_utils.array_io_utils import lined_file_to_array
from nlp.feature_extractors.feature_extractor import FeatureExtractor
import re

CLAUSE_PUNCT = ['but', '.', ';']  # Identifiy clausal breaks
NEG_WORDS = list(lined_file_to_array('nlp/negation_words.txt'))  # Negation words
FEATURE_LENGTH = 4

class NegationFeatureExtractor(FeatureExtractor): 
    """
    Extracts negated features, for now as list.
    """

    def get_features(self, text):
        """ text - string of text document """
        # Split text into list of words and punctuation
        split_text = re.findall(r"[\w']+|[.,!?;]", text)
        negated_words = [[]] # different sublist per clause
        negated_features = []
        results = []
        scope_is_neg = False
        idx = 0
        for i, word in enumerate(split_text):
            # Update negation scope
            if word in NEG_WORDS:
                scope_is_neg = not scope_is_neg
            
            # If new clause, reset to no negation and start new sublist
            elif word in CLAUSE_PUNCT:
                scope_is_neg = False
                negated_words.append([])
                idx += 1
            
            # While negation scope is true, words are negated
            else:
                if scope_is_neg:
                    negated_words[idx].append(word) 

        # Now we have negated words, identify negated features (multiple words)
        for feature in self._keyword_handler.keywords:
            # Look for consecutive words representing a feature
            for clause_list in negated_words:
                for wsize in range(0, FEATURE_LENGTH+1):
                    left = 0
                    right = wsize
                    while right < len(clause_list) + 1:
                        feature_count = 0
                        # Every word in window must be part of set of words for the feature
                        for i in range(left, right):
                            if clause_list[i] in feature:
                                feature_count += 1
                        if feature_count == len(feature):
                            negated_features.append(feature)
                        left += 1
                        right += 1
        # clean up
        result = []
        for item in negated_features:
            if item not in result and len(item)>0:
                result.append(item)
        return result

