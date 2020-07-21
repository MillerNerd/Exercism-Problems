import re


def is_valid(isbn):
    check = isbn[-1:]
    isbn = list(map(int, re.sub('[^0-9]', '', isbn[:-1])))
    check = re.sub('[^0-9xX]', '', check)
    if not check:
        return False
    if len(isbn) != 9:
        return False
    if check == 'X':
        check = '10'
    check = int(check)
    for i in range(9):
        check += isbn[i] * (10 - i)
    if check % 11:
        return False
    return True
