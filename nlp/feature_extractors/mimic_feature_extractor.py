""" Class definition for MimicFeatureExtractor.
"""
from file_utils.array_io_utils import read_array
from nlp.stanza_utils import get_stanza_model
from preprocessing.string_cleaning_utils import (get_punctuation,
                                                 get_stopwords,
                                                 remove_stopchars,
                                                 remove_stopstrings, stem)
from nlp.feature_extractors.feature_extractor import FeatureExtractor

class MimicFeatureExtractor(FeatureExtractor): 
    """Extracts keywords based on what stanza tags as a keyword, which 
    uses the MIMIC clinical feature dataset.
    """
    
    def get_features(self, text):
        nlp = get_stanza_model(
            package='mimic', processors={'ner': 'i2b2'}, download=False
        )
        doc = nlp(text)
        result = []

        # Loop through all the entities found in the text.
        for ent in doc.entities:
            # Construct a set of cleaned words from entity.
            words = ent.text.split(' ')
            words = remove_stopstrings(words, self._keyword_handler.stopwords)
            words = [remove_stopchars(word, self._keyword_handler.punctuation) for word in words]
            words = [stem(word) for word in words]
            words_set = set(words)
            # Loop through all our stored clinical features.
            for feature in self._keyword_handler.keywords:
                # Check that all the words in the feature are in the set.
                valid_feature = True
                for word in feature:
                    if word not in words_set:
                        valid_feature = False
                # If all words are found then this is likley to be a valid feature.
                if valid_feature and len(feature) > 0:
                    result.append(feature)
        return result
