import unittest
from nlp.feature_extractors.mimic_feature_extractor import MimicFeatureExtractor
from nlp.keyword_handler import KeywordHandler

class TestFeatureExtraction(unittest.TestCase):
    
    def test(self):
        test_text = 'The patient has pain in his arm, leg, and chest.'
        kh = KeywordHandler()
        ff = MimicFeatureExtractor(kh)
        features = ff.get_features(test_text)
        self.assertIsNotNone(features)

if __name__ == '__main__':
    unittest.main()

        
