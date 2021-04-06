""" Class definition for DataModel.
"""

from abc import ABC, abstractmethod

class DataModel(ABC):
    """ A DataModel represents a feature extraction method, usually 
    made up of a combination of feature extractors. The DataModel is 
    in charge of storing & returning these feature extractors.
    """
    
    @abstractmethod
    def get_feature_extractors():
    """ Return the feature extractors of the DataModel.
    """
        pass   


