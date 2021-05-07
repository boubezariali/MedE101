""" Class definition for DataModel.
"""

from abc import ABC, abstractmethod

from nlp.keyword_handler import KeywordHandler
from nlp.modifier_handler import ModifierHandler

class DataModel(ABC):
    """ A DataModel represents a feature extraction method, usually 
    made up of a combination of feature extractors. The DataModel is 
    in charge of storing & returning these feature extractors.
    """
    def __init__(self):
        """ Initialize the keyword handler and modifier handler to 
        write information to using the extractors. 
        """
        self._modifier_handler = ModifierHandler()
        self._keyword_handler = KeywordHandler()
    
    @abstractmethod
    def get_feature_extractors():
        """ Return the feature extractors of the DataModel.
        """
        pass   

    def get_modifier_extractors():
        """ Return the  modifier extractors of the DataModel.
        """
        pass


