""" 
Class definition for NegationFeatureExtractor.
"""
from file_utils.array_io_utils import lined_file_to_array
from nlp.feature_extractors.feature_extractor import FeatureExtractor

CLAUSE_PUNCT = ['but', '.', ';']  # Identifiy clausal breaks
NEG_WORDS = list(lined_file_to_array('nlp/negation_words.txt'))  # Negation words

class NegationFeatureExtractor(FeatureExtractor): 
    """
    Extracts negated features, for now as list.
    """

    def get_features(self, text):
        negated = []
        scope_is_neg = False
        for i, word in enumerate(text):
            # Update negation scope
            if word in NEG_WORDS:
                scope_is_neg = not scope_is_neg
            
            # If new clause, reset to no negation
            elif word in CLAUSE_PUNCT:
                scope_is_neg = False
            
            # While negation scope is true, words are negated
            else:
                if scope_is_neg:
                    # We only want negated features
                    if word in self._keyword_handler.keywords:
                        negated.append(word)
        return negated       

