""" Class definition for base ModifierExtractor.
"""
from collections import defaultdict

from nlp.stanza_utils import get_stanza_model


class ModifierHandler:
    """ This class stores modifiers in a indexed map. 
    """

    def __init__(self):
        # Initialize the map such that each word represents a list.
        self._modifiers = defaultdict(list)

    def add_modifier(self, sent_idx, word_idx, modifier):
        """ Add a modifier to a word.
        
        Args: 
            sent_idx: int representing which sentence the word is in.
            word_idx: int identifying the word within the sentence.
            modifier: string modifier.
        """
        self._modifiers[(sent_idx, word_idx)].append(modifier)

    def get_modifier(self, sent_idx, word_idx):
        """ Access the modifiers of a word.

        Args:
            sent_idx: int representing which sentence the word is in.
            word_idx: int identifying the word within the sentence.

        Returns:
            list of modifiers.
        """
        if (sent_idx, word_idx) in self._modifiers:
            return self._modifiers[sent_idx, word_idx]
        return []

    @property
    def modifiers(self):
        """ Getter function for the modifier map.
        """
        return self._modifiers
