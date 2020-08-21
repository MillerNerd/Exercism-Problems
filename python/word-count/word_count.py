from collections import Counter
import re


def count_words(sentence):
    # make lowercase because case-insensitive (and answers look for lowercase)
    answer = sentence.lower()
    # remove characters we don't care about and split into a list of words delimited by characters/whitespace
    # we will get to apostrophe later, because contractions
    answer = re.split('[\s,.?!&@$%^&:_]', answer)
    # remove empty strings in list left by re.split
    answer = filter(None, answer)
    # strip apostrophes, which leaves contractions/possessives but removes single-quotes
    answer = [a.strip("'") for a in answer]
    # count up matching words, returns dict
    return Counter(answer)
