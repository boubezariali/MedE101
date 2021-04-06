""" Main binary file for feature extraction.
"""

import argparse

from nlp.data_models.comprehensive_data_model import ComprehensiveDataModel
from nlp.data_module import DataModule


def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_text",
        type=str,
        help="Path of text to extract on.",
        default="data/test_data/raw_text/Coronary_Artery_Disease.txt",
    )
    args = parser.parse_args()

    model = ComprehensiveDataModel()
    module = DataModule(model, args.input_text)
    features = module.generate_features()
    print(features)

if __name__ == "__main__":
    main()
