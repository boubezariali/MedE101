""" Class definition for ComprehensiveDataModel.
"""

from nlp.data_models.data_model import DataModel
from nlp.feature_extractors.mimic_feature_extractor import MimicFeatureExtractor 
from nlp.feature_extractors.anatomy_list_feature_extractor import AnatomyListFeatureExtractor
from nlp.feature_extractors.clause_feature_extractor import ClauseFeatureExtractor
from nlp.modifier_extractors.negation_modifier_extractor import NegationModifierExtractor


class ComprehensiveDataModel(DataModel):
    """ This data model uses all feature extractors except for the 
    negation feature extractor (proper output format for it not determined yet).
    """
    def get_feature_extractors(self):
        return [MimicFeatureExtractor(self._keyword_handler, self._modifier_handler), 
                AnatomyListFeatureExtractor(self._keyword_handler, self._modifier_handler), 
                ClauseFeatureExtractor(self._keyword_handler, self._modifier_handler)] 

    def get_modifier_extractors(self):
        return [NegationModifierExtractor(self._keyword_handler, self._modifier_handler)]

    
