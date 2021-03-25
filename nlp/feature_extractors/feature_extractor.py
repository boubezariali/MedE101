""" Class definition for base FeatureExtractor.
"""
from abc import ABC, abstractmethod

from nlp.keyword_handler import KeywordHandler


class FeatureExtractor(ABC):
    """Base class for all feature extractors. A feature extactor is a 
    object that parses text and outputs a list of features it finds using 
    a specific technique.
    """
    def __init__(self, keyword_handler):
        """Initializes the core funtionality using the KeywordHandler.
        Args:
           keyword_handler: KeywordHandler 
        """
        self._keyword_handler = keyword_handler

    @abstractmethod
    def get_features():
        """This function should return a list of features from the KeyWordHandler found 
        by the extractor.
        Returns:
            list of strings
        """
        pass
