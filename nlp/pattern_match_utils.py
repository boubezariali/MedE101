import pandas as pd
from rake_nltk import Rake

import file_utils.array_io_utils as utils

CLAUSE_PUNCT = [',', '.', ';']  # Identifiy clausal breaks
NEG_WORDS = list(utils.lined_file_to_array('nlp/negation_words.txt'))  # Negation words


def load_tags(tag_file='main_data/scraped_clinical_keywords.csv'):
    """
    Loads file of clinical features (NLP tags) into dataframe,
    cleans any missing data, outputs dict of tag:index
    """
    df = pd.read_csv(tag_file)
    df.dropna()
    dic = {}
    for i, row in enumerate(df):
        dic[row] = i
    return dic


def pattern_match_window(text, tags, label, output_path, w=4):
    """
    Function to match patterns in text and identity training data using sliding window.
    Inputs:
      - text: array of processed text
      - tags: dict of NLP tags to look for
      - w: window size to look for in sentence
      - output_path: where to output training data
    """
    # Each feature corresponds to tag i, index j = tag[i]
    datapoint = [0] * (len(tags) + 1)
    datapoint.append(label)

    # For each sentence in the array
    for line in text:
        # Break sentence by space
        sentence = line.split(" ")
        sentence = mark_negation(sentence)

        # Slide windows size 1...w
        for k in range(0, w + 1):
            left = 0
            right = k
            while right < len(sentence) + 1:
                phrase = " ".join(sentence[left:right])
                if phrase in tags:
                    datapoint[tags[phrase]] = 1
                left += 1
                right += 1

    # Add datapoint to training data file
    utils.add_line_to_file(output_path, datapoint)


def pattern_match_keyword(text, tags, label, output_path):
    """
    Function to match patterns in text and identity training data using keywords.
    Inputs:
      - text: array of sentences processed by preprocessing_main
      - tags: dict of NLP tags to look for
      - output_path: where to output training data
    """
    raker = Rake()

    # Each feature corresponds to tag i, index j = tag[i]
    datapoint = [0] * (len(tags) + 1)  # how to incorporate disease label?
    datapoint.append(label)

    # For each sentence in the dataframe
    for sentence in text:
        # print("sentence", sentence)
        raker.extract_keywords_from_text(sentence)
        keywords = raker.get_ranked_phrases()
        # print("keywords:", keywords)

        # Check if keywords are in
        for k in keywords:
            if k in tags:
                datapoint[tags[k]] = 1

    # Add datapoint to training data file
    utils.add_line_to_file(output_path, datapoint)


def mark_negation(sentence):
    """
    Marks words that are negated in meaning. Double negatives are positive.
    Inputs:
      - sentence: list of words representing split sentence
      - verbose: print negated sentence output
    Output:
      - sentence with negated words suffixed by "_NEG"
    Example input: ["she", "did", "not", "feel", "pain"]
    Example output: ["she", "did", "not", "feel_NEG", "pain_NEG"]
    """
    scope_is_neg = False
    for i, word in enumerate(sentence):
        # If negation word, then negation scope flips
        if word in NEG_WORDS:
            scope_is_neg = not scope_is_neg

        # If new clause, then negation scope resets to false
        elif word in CLAUSE_PUNCT:
            scope_is_neg = False

        # While negation scope is true, words are negated
        else:
            if scope_is_neg:
                print("neg_scope:", sentence[i])
                sentence[i] += "_NEG"
    return sentence
