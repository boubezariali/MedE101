""" 
Class definition for NegationModifierExtractor
"""
from file_utils.array_io_utils import lined_file_to_array
from nlp.modifier_extractors.modifier_extractor import ModifierExtractor
from nlp.stanza_utils import get_stanza_model
import re
from preprocessing.string_cleaning_utils import (get_punctuation,
                                                 get_stopwords,
                                                 remove_stopchars,
                                                 remove_stopstrings, stem)

CLAUSE_PUNCT = ['but', '\.', ';']  # Identifiy clausal breaks
NEG_WORDS = set(lined_file_to_array('nlp/negation_words.txt'))  # Negation words

class NegationModifierExtractor(ModifierExtractor):
    """
    Extracts all negated words, for now as list.
    """

    def get_modifiers(self, text):
        """ text - string of text document """
        nlp = get_stanza_model(processors='tokenize', download=False)
        doc = nlp(text) 
        result = []
        # Get all sentences in the input text.
        sentences = [sentence.text for sentence in doc.sentences]
        
        for sent_idx, sentence in enumerate(sentences):
            # Split the sentence into its clauses seperated by the clause punctutation.
            clauses = re.split('|'.join(CLAUSE_PUNCT), sentence)

            word_idx = 0
            for clause in clauses:  
                # Clean up each clause.
                clause = clause.split(' ')
                is_neg = False
                for word in clause: 
                    if is_neg: 
                        result.append(word)
                        self._modifier_handler.add_modifier(sent_idx, word_idx, 'neg')
                    if word in NEG_WORDS:
                       is_neg = True
                    word_idx += 1
