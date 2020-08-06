import collections
import re


def count_words(sentence):
    return collections.Counter([a.strip("'") for a in list(filter(None, re.split('[\s,.?!&@$%^&:_]', sentence.lower())))])
