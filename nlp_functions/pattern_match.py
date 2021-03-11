'''
Generate training data from preprocessed medical text, via pattern-matching.

Example usage: bazel-bin/nlp_functions/pattern_match
                --input_text=sample_text.csv 
                --label="heart disease"
                --tags=sample_tags.csv
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

Pattern matchin methods:
    pattern_match_window: works pretty well with sliding window, will identify all verbatim tags
    pattern_match_keyword: needs work identifying correct keywords

TODO: incorporate negation detection
'''
import pandas as pd
import argparse
from rake_nltk import Rake
import file_utils.array_io_utils as utils 

def load_tags(tag_file='main_data/scraped_clinical_keywords.csv'):
    '''
    Loads file of clinical features (NLP tags) into dataframe,
    cleans any missing data, outputs dict of tag:index
    '''
    df = pd.read_csv(tag_file)
    df.dropna()
    dic = {}
    for i, row in enumerate(df):
        dic[row] = i
    return dic

def pattern_match_window(text, tags, label, output_path, w=4):
    '''
    Function to match patterns in text and identity training data using sliding window.
    Inputs: 
      - text: array of processed text
      - tags: dict of NLP tags to look for
      - w: window size to look for in sentence
      - output_path: where to output training data
    '''
    # Each feature corresponds to tag i, index j = tag[i]
    datapoint = [0] * (len(tags) + 1)
    datapoint.append(label)

    # For each sentence in the array
    for line in text:
        # Break sentence by space
        sentence = line.split(" ")

        # Slide windows size 1...w
        for k in range(0, w+1):
            left = 0
            right = k
            while right < len(sentence)+1:
                phrase = " ".join(sentence[left:right])
                #print(phrase)
                if phrase in tags:
                    datapoint[tags[phrase]] = 1
                left += 1
                right += 1
    
    # Add datapoint to training data file
    utils.add_line_to_file(output_path, datapoint)

def pattern_match_keyword(text, tags, label, output_path):
    '''
    Function to match patterns in text and identity training data using keywords.
    Inputs: 
      - text: array of sentences processed by preprocessing_main
      - tags: dict of NLP tags to look for
      - output_path: where to output training data
    '''
    raker = Rake()

    # Each feature corresponds to tag i, index j = tag[i]
    datapoint = [0] * (len(tags) + 1) # how to incorporate disease label?
    datapoint.append(label)

    # For each sentence in the dataframe
    for sentence in text:
        #print("sentence", sentence)
        raker.extract_keywords_from_text(sentence)
        keywords = raker.get_ranked_phrases()
        #print("keywords:", keywords)

        # Check if keywords are in 
        for k in keywords:
            if k in tags:
                datapoint[tags[k]] = 1

    # Add datapoint to training data file
    utils.add_line_to_file(output_path, datapoint)



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

    parser.add_argument(
        "--label",
        type=str,
        help="Label for training data"
    )

    parser.add_argument(
        "--method",
        type=str,
        default="window",
        help="Either 'window' or 'keyword' for pattern matching method"
    )

    parser.add_argument(
        "--wsize",
        type=int,
        help="Optional window size for window method."
    )
    args = parser.parse_args()
    assert args.input_text is not None, "Input text file must be non-empty"
    assert args.output is not None, "Output location must be non-empty"
    assert args.label is not None, "Must include label for this training point"
    
    text_obj = utils.csv_to_list(args.input_text)
    #print("text:", text_obj)
    tags = load_tags(args.tags)
    #print("tags:", tags)

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


