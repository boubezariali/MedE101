""" Simple unit test to check codebase stability.
"""

import unittest
from nlp.feature_extractors.mimic_feature_extractor import MimicFeatureExtractor
from nlp.keyword_handler import KeywordHandler

class TestFeatureExtraction(unittest.TestCase):
    
    def test(self):
        kh = KeywordHandler()
        self.assertIsNotNone(kh)

if __name__ == '__main__':
    unittest.main()

        
