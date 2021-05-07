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
        cur_idx = 0
        cur_term = doc.entities[cur_idx].text.split(' ')
        for sent_idx, sentence in enumerate(doc.sentences):
            words = [word.text for word in sentence.words]

            for word_idx, word in enumerate(words):
                if word_idx + len(cur_term) <= len(words) and cur_term == words[word_idx:(word_idx + len(cur_term))]: 
                    if cur_idx < len(doc.entities):
                        cur_term = doc.entities[cur_idx].text.split(' ')
                        cur_term = remove_stopstrings(words, self._keyword_handler.stopwords)
                        cur_term = [remove_stopchars(word, self._keyword_handler.punctuation) for word in words]
                        cur_term = [stem(word) for word in words]
                        term_set = set(cur_term)
                        found_feature = self.find_feature(term_set)
                        if found_feature:
                            positive = 'neg' not in self._modifier_handler.get_modifier(sent_idx, word_idx)
                            self._keyword_handler.set(found_feature, val=positive)
                    cur_idx += 1

    def find_feature(self, words_set):
        # Loop through all our stored clinical features.
        for feature in self._keyword_handler.keywords:
            # Check that all the words in the feature are in the set.
            valid_feature = True
            for word in feature:
                if word not in words_set:
                    valid_feature = False
            # If all words are found then this is likley to be a valid feature.
            if valid_feature and len(feature) > 0:
                return feature
        return None
        

