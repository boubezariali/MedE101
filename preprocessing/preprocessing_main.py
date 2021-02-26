""" Binary to preprocess medical literature. 
"""
from preprocessing.sentence_splitting_utils import *
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--split_method",
        type=str,
        help="Sentence splitting method to use. Can be regex or nltk",
    )
    parser.add_argument("--input_file", type=str, help="Path of file to process.")
    parser.add_argument(
        "--output_file", type=str, default="", help="Output location of processed text."
    )
    args = parser.parse_args()
    assert args.input_file is not None, "Input file must be non-empty"

    # Read the file and split it. 
    with open(args.input_file, "r") as f:
        text = f.read()
    if args.split_method == "regex":
        split_data = split_into_sentences_regex(text)
    elif args.split_method == "nltk":
        split_data = split_into_sentences_nltk(text)
    else:
        raise ValueError("Invalid option {}.".format(args.split_method))
    # Write out the sentences, one per line to the output file. 
    with open(args.output_file, "w") as f:
        result = "\n".join(split_data)
        f.write(result)


if __name__ == "__main__":
    main()
