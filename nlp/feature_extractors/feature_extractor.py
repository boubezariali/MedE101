import re

import glog

from abc import ABC, abstractmethod
from nlp.keyword_handler import KeywordHandler

class FeatureExtractor(ABC):

    def __init__(self, keyword_handler):
        self._keyword_handler = keyword_handler
    
    @abstractmethod
    def get_features():
        pass
    

