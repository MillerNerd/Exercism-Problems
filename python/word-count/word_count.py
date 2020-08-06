import collections
import re


def count_words(sentence):
    print('\n', sentence, '\n')
    print((list(filter(None, re.split('[\s,.?!&@$%^&:_]', sentence.lower())))))
    return collections.Counter((list(filter(None, re.split('[\s,.?!&@$%^&:_]', sentence.lower())))))
