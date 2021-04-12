""" Class definition for DataModule.
"""


class DataModule:
    """ The DataModule is in charge of taking the outputs of various feature extractors
    and combining them into one consistent data structure.
    TODO(aboubezari): add isinstance assert.

    Args: 
        data_model: DataModel to be used
        text_path: string path to the text to be processed.
    """

    def __init__(self, data_model, text_path):
        self._data_model = data_model
        self._text_path = text_path

    def generate_features(self):
        """ Generates a set of unique features from all the feature extractors of the 
        data model.

        Returns: 
            set of unique features.
        """

        with open(self._text_path) as f:
            text = f.read()

        feature_extractors = self._data_model.get_feature_extractors()
        result = set()
        for feature_extractor in feature_extractors:
            for term in feature_extractor.get_features(text):
                result.add(term)
        return result
