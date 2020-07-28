import re


def is_isogram(string):
    # remove non-letter characters and set characters to lowercase
    string = re.sub('[^a-z]', "", string.lower())
    # if any character has a count > 1, string is not an isogram
    for letter in string:
        if string.count(letter) > 1:
            return False
    # all tests passed
    return True
