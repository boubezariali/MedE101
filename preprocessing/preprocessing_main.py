""" Binary to preprocess medical literature. 

Example usage: bazel-bin/preprocessing/preprocessing_main 
                --input_file=RCode/data/Acute_Coronary_Syndromes.txt 
                --output_file=preprocessing/test.txt 
                --split_method=regex
"""
import argparse

from preprocessing import sentence_splitting_utils
from preprocessing import string_cleaning_utils
from file_utils.delimeted_file import DelimetedFile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--split_method",
        type=str,
        default="regex",
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
    # Join the sentences with commas.
    tokenized_data = [",".join(lst) for lst in tokenized_data]

    # Write the list of sentences to disk.
    df = DelimetedFile(args.output_file, overwrite=True)
    df.add(tokenized_data)
    df.write()


if __name__ == "__main__":
    main()
