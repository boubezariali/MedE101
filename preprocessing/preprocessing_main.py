""" Binary to preprocess medical literature. 

Example usage: bazel-bin/preprocessing/preprocessing_main 
                --input_file=RCode/data/Acute_Coronary_Syndromes.txt 
                --output_file=preprocessing/test.txt 
                --split_method=regex
"""
import argparse

from preprocessing import sentence_splitting_utils
from preprocessing import string_cleaning_utils


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
        "--output_file", type=str, default="preprocessing/test.txt", help="Output location of processed text."
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

    punctuation = string_cleaning_utils.get_punctuation() 
    stopwords = string_cleaning_utils.get_stopwords() 
    
    tokenized_data = [string_cleaning_utils.word_tokenize(s) for s in split_data]
    tokenized_data = [string_cleaning_utils.remove_stopstrings(lst, punctuation) for lst in tokenized_data]
    tokenized_data = [string_cleaning_utils.remove_stopstrings(lst, stopwords) for lst in tokenized_data]

    # Write out the sentences, one per line to the output file. 
    with open(args.output_file, "w") as f:
        for s in tokenized_data: 
            line = ','.join(s)
            f.write(line + '\n')

if __name__ == "__main__":
    main()
