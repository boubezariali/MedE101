###############################################################
# Function to match patterns in text and identity training data
# Inputs:
# - txt block to ingest
# - CSV of NLP tags - default 'main_data/scraped_clinical_keywords.csv'

def pattern_match(text_file, tag_file):
    return