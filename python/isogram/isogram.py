import re


def is_isogram(string):
    string = re.sub(r'[^a-zA-Z]', "", string.lower())
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True
