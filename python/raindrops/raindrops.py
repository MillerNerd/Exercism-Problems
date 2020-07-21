def convert(number):
    lst = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    answer = ''
    for key, value in lst.items():
        if number % key == 0:
            answer += value
    if not answer:
        answer = str(number)
    return answer
