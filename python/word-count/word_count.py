from collections import Counter
import re


def count_words(sentence):
    answer = sentence.lower()
    answer = re.split('[\s,.?!&@$%^&:_]', answer)
    answer = (x for x in answer if x is not '')
    answer = (a.strip("'") for a in answer)
    return Counter(answer)
