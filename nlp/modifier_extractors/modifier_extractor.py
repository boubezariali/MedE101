""" Class definition for base ModifierExtractor.
"""
from abc import ABC, abstractmethod

import numpy as np

class ModifierExtractor(ABC):
    """ This class is responsible for finding modifiers for each word 
    in a given text.
    """

    def __init__(self, keyword_handler, modifier_handler):
        """ The class requires a KeywordHandler for string cleaning and
        a ModifierHandler to store the extracted modifiers.

        Args:
            keyword_handler: KeywordHandler
            modifier_handler: ModifierHandler
        """
        self._keyword_handler = keyword_handler
        self._modifier_handler = modifier_handler        
    
    @abstractmethod
    def get_modifiers(self, text):
        """ This function will extract all modifiers and store them in
        the ModifierHandler attribute.
        """
        pass
        


