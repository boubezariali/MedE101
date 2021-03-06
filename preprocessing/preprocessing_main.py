""" Binary to preprocess medical literature. 

Example usage: bazel-bin/preprocessing/preprocessing_main
                --input_file=extra_data/Acute_Coronary_Syndromes.txt
                --output_dir=preprocessing/preprocessed_test_data
                --split_method=nltk
"""
import argparse
import os
import sys

import glog as log
import numpy as np

from file_utils.array_io_utils import write_array
from preprocessing import sentence_splitting_utils
from preprocessing import string_cleaning_utils as ss


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--split_method",
        type=str,
        default="nltk",
        help="Sentence splitting method to use. Can be regex or nltk",
    )
    parser.add_argument("--input_file", type=str, help="Path of file to process.")
    parser.add_argument("--input_dir", type=str, help="Directory of files to process.")
    parser.add_argument(
        "--output_dir",
        type=str,
        default="preprocessing/TEST_preprocessing_main_output.txt",
        help="Output location of processed text.",
    )
    args = parser.parse_args()

    assert (args.input_file is not None) ^ (
        args.input_dir is not None
    ), "One of input_file or input_dir must be non-empty"
    input_dir = (
        args.input_dir
        if args.input_dir is not None
        else os.path.dirname(args.input_file)
    )

    filenames = []
    if args.input_file is not None:
        assert os.path.isfile(args.input_file), "Not a file: {}".format(args.input_file)
        filenames = [os.path.basename(args.input_file)]
    else:
        assert os.path.isdir(args.input_dir), "Not a directory: {}".format(
            args.input_dir
        )
        _, _, filenames = next(os.walk(input_dir))

    # Read in the files.
    for filename in filenames:
        log.info("Processing {}".format(os.path.join(input_dir, filename)))
        with open(os.path.join(input_dir, filename), "r") as f:
            text = f.read()

        text = ss.strip_html_tags(text)
        text = ss.remove_accented_chars(text)
        text = ss.expand_contractions(text)

        with open(os.path.join(args.output_dir, filename), 'w') as f:
            f.write(text)


if __name__ == "__main__":
    main()
