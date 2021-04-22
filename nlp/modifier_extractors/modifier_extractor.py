""" Class definition for base ModifierExtractor.
"""
from abc import ABC, abstractmethod

import numpy as np

class ModifierExtractor(ABC):

    def __init__(self, keyword_handler, modifier_handler):
        self._modifiers = set()
        self._keyword_handler = keyword_handler
        self._modifier_handler = modifier_handler
        
    
    @abstractmethod
    def get_modifiers(self, text):
        pass
        


