""" Class definition for AnatomyListExtractor.
"""
import numpy as np
from collections import defaultdict

from file_utils.array_io_utils import read_array
from nlp.stanza_utils import get_stanza_model
from preprocessing.string_cleaning_utils import (get_punctuation,
                                                 get_stopwords,
                                                 remove_stopchars,
                                                 remove_stopstrings, stem)
from nlp.feature_extractors.feature_extractor import FeatureExtractor

LIST_HEADS = set(['nmod', 'obl', 'obj'])
PROBLEMS = set(['pain', 'discomfort', 'radiate'])

class AnatomyListFeatureExtractor(FeatureExtractor): 
    """Extracts keywords from lists of anatomical nouns.
    """
    
    def get_features(self, text):
        result = []
        nlp_anatem = get_stanza_model(package='mimic', processors={'ner': 'anatem'}, download=False)
        doc_anatem = nlp_anatem(text) 
        anatomy_dict = self._get_term_dict([ent.text for ent in doc_anatem.entities])
        
        # Get all sentences in the input text.
        sentences = [sentence.words for sentence in doc_anatem.sentences]
        for sentence in sentences:
            i = len(sentence) - 1
            lists = []
            while i >= 0:
                cur_list = []
                while i >= 0:
                    word = sentence[i]
                    # Check if the word is part of a list and is a body part.
                    found_term = self._find_word(sentence, i, anatomy_dict)
                    if word.deprel == 'conj' and found_term is not None:
                        cur_list.append(found_term)
                    # Check if the word is a list head, for that to be true there needs to be a non-zero length list already.
                    elif word.deprel in LIST_HEADS and found_term is not None and len(cur_list) > 0:
                        cur_list.append(found_term)
                        j = i - 1
                        while j >= 0: 
                            word = sentence[j] 
                            if stem(word.text) in PROBLEMS:
                                cur_list.append(stem(word.text))
                                break
                            j -= 1
                        break
                    i -= 1

                if len(cur_list) > 0:
                    lists.append(np.copy(cur_list))
                i -= 1
        return lists

    def _get_term_dict(self, terms):
        result = defaultdict(list)
        for term in terms:
            words = term.split(' ')
            words.reverse()
            result[words[0]].append(words)
        return result
         

    def _find_word(self, sentence, i, term_dict):
        terms = term_dict[sentence[i].text]
        for lst in terms:
            match = True
            for j, word in enumerate(lst):
                if word != sentence[i - j].text:
                    match = False
            if match:
                return ' '.join(lst)
        return None 
