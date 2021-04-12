""" Class definition for ComprehensiveDataModel.
"""

from nlp.data_models.data_model import DataModel
from nlp.keyword_handler import KeywordHandler
from nlp.feature_extractors.mimic_feature_extractor import MimicFeatureExtractor 
from nlp.feature_extractors.anatomy_list_feature_extractor import AnatomyListFeatureExtractor
from nlp.feature_extractors.clause_feature_extractor import ClauseFeatureExtractor

class ComprehensiveDataModel(DataModel):
    """ This data model uses all feature extractors except for the 
    negation feature extractor (proper output format for it not determined yet).
    """
    def get_feature_extractors(self):
        kh = KeywordHandler()
        return [MimicFeatureExtractor(kh), AnatomyListFeatureExtractor(kh), ClauseFeatureExtractor(kh)] 
