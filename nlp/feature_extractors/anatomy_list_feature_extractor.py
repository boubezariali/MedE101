""" Class definition for AnatomyListExtractor.
"""
import numpy as np
from file_utils.array_io_utils import read_array
from nlp.stanza_utils import get_stanza_model
from preprocessing.string_cleaning_utils import (get_punctuation,
                                                 get_stopwords,
                                                 remove_stopchars,
                                                 remove_stopstrings, stem)
from nlp.feature_extractors.feature_extractor import FeatureExtractor

class AnatomyListFeatureExtractor(FeatureExtractor): 
    """Extracts keywords from lists of anatomical nouns.
    """
    
    def get_features(self, text):
        nlp = get_stanza_model(package='mimic', processors={'ner': 'anatem'}, download=False)
        doc = nlp(text) 
        result = []

        # Get all sentences in the input text.
        sentences = [sentence.words for sentence in doc.sentences]
        anatomy_terms = set([ent.text for ent in doc.entities])
        print('anatomy terms:', anatomy_terms)
        
        for sentence in sentences:
            i = len(sentence) - 1
            lists = []
            while i >= 0:
                cur_list = []
                while i >= 0:
                    word = sentence[i]
                    if word.deprel == 'conj' and word.text in anatomy_terms:
                        cur_list.append(word.text)
                    elif word.deprel == 'obl' and word.text in anatomy_terms:
                        cur_list.append(word.text)
                        break
                    i -= 1

                lists.append(np.copy(cur_list))
                i -= 1
            print('list:', lists)

                     
                
                
            
