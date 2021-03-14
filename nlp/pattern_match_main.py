'''
Generate training data from preprocessed medical text, via pattern-matching.

Example usage: bazel-bin/nlp_functions/pattern_match
                --input_text=nlp_functions/sample_text.csv 
                --label="heart disease"
                --tags=nlp_functions/sample_tags.csv
                --output=dummyoutput.txt
                --method=window
                --wsize=3
After running, you should see an additional line added to the training data output

Params:
    input_text: path to already preprocessed text csv file
    label: label for the training point, a disease name
    tags: path to csv of NLP tags (clinical features)
    output: training data file, where to append a datapoint
    method: which pattern matching method to use (window or keyword)
    wsize: optional size of window for window method

Pattern matching methods:
    pattern_match_window: works pretty well with sliding window, will identify all verbatim tags
    pattern_match_keyword: needs work identifying correct keywords

TODO: incorporate negation detection
'''

import argparse

import file_utils.array_io_utils as utils
from nlp.pattern_match_utils import (load_tags,
                                               pattern_match_keyword,
                                               pattern_match_window)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_text",
        type=str,
        help="Path of already preprocessed file to use as textual data",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output location of processed data.",
    )
    parser.add_argument(
        "--tags",
        type=str,
        default="main_data/scraped_clinical_keywords.csv",
        help="Path of CSV with NLP tags.",
    )

    parser.add_argument("--label", type=str, help="Label for training data")

    parser.add_argument(
        "--method",
        type=str,
        default="window",
        help="Either 'window' or 'keyword' for pattern matching method",
    )

    parser.add_argument(
        "--wsize", type=int, help="Optional window size for window method."
    )
    args = parser.parse_args()
    assert args.input_text is not None, "Input text file must be non-empty"
    assert args.output is not None, "Output location must be non-empty"
    assert args.label is not None, "Must include label for this training point"

    # text_obj = utils.csv_to_list(args.input_text)
    text_obj = utils.read_array(args.input_text)
    print("text:", text_obj)
    tags = load_tags(args.tags)
    # print("tags:", tags)

    if args.method == "window":
        if args.wsize is not None:
            pattern_match_window(text_obj, tags, args.label, args.output, w=args.wsize)
        else:
            pattern_match_window(text_obj, tags, args.label, args.output)
    elif args.method == "keyword":
        pattern_match_keyword(text_obj, tags, args.label, args.output)
    print("after pattern match")


if __name__ == "__main__":
    main()
