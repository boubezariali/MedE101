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

class AnatomyListFeatureExtractor(FeatureExtractor): 
    """Extracts keywords from lists of anatomical nouns.
    """
    
    def get_features(self, text):
        nlp = get_stanza_model(package='mimic', processors={'ner': 'anatem'}, download=False)
        doc = nlp(text) 
        result = []

        # Get all sentences in the input text.
        sentences = [sentence.words for sentence in doc.sentences]
        anatomy_terms = [ent.text for ent in doc.entities]
        anatomy_dict = defaultdict(list)
        for ent in doc.entities:
            words = ent.text.split(' ')
            words.reverse()
            anatomy_dict[words[0]].append(words)
        
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
                        break
                    i -= 1

                if len(cur_list) > 0:
                    lists.append(np.copy(cur_list))
                i -= 1

    def _find_word(self, sentence, i, anatomy_dict):
        terms = anatomy_dict[sentence[i].text]
        for lst in terms:
            match = True
            for j, word in enumerate(lst):
                if word != sentence[i - j].text:
                    match = False
            if match:
                return ' '.join(lst)
        return None
                    

                     
                
                
            
