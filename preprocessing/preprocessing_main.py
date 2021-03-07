""" Binary to preprocess medical literature. 

Example usage: bazel-bin/preprocessing/preprocessing_main
                --input_file=extra_data/Acute_Coronary_Syndromes.txt
                --output_file=preprocessing/TEST_preprocessing_main.txt
                --split_method=nltk
"""
import argparse
import numpy as np
import glog as log

from file_utils import array_io_utils 
from preprocessing import sentence_splitting_utils, string_cleaning_utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--split_method",
        type=str,
        default="nltk",
        help="Sentence splitting method to use. Can be regex or nltk",
    )
    parser.add_argument("--input_file", type=str, help="Path of file to process.")
    parser.add_argument(
        "--output_file",
        type=str,
        default="preprocessing/TEST_preprocessing_main_output.txt",
        help="Output location of processed text.",
    )
    args = parser.parse_args()
    assert args.input_file is not None, "Input file must be non-empty"

    log.info("Processing {}".format(args.input_file))

    # Read the file and split it.
    with open(args.input_file, "r") as f:
        text = f.read()
    if args.split_method == "regex":
        split_data = sentence_splitting_utils.split_into_sentences_regex(text)
    elif args.split_method == "nltk":
        split_data = sentence_splitting_utils.split_into_sentences_nltk(text)
    else:
        raise ValueError("Invalid option {}.".format(args.split_method))

    # Get the punctuation and stopwords to remove.
    punctuation = string_cleaning_utils.get_punctuation()
    stopwords = string_cleaning_utils.get_stopwords()
    # Tokenize into individual words.
    tokenized_data = [string_cleaning_utils.word_tokenize(s) for s in split_data]
    # Remove punctuation.
    tokenized_data = [
        string_cleaning_utils.remove_stopstrings(lst, punctuation)
        for lst in tokenized_data
    ]
    # Remove stopwords
    tokenized_data = [
        string_cleaning_utils.remove_stopstrings(lst, stopwords)
        for lst in tokenized_data
    ]

    # Write the list of sentences to disk.
    array_io_utils.write_array(args.output_file, tokenized_data)
    
    log.info("Successfully processed output to {}".format(args.output_file))


if __name__ == "__main__":
    main()
