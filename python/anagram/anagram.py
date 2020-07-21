def find_anagrams(word, candidates):
    answer = []
    for i in candidates:
        if sorted(word.lower()) == sorted(i.lower()):
            if word.lower() != i.lower():
                answer.append(i)
    return answer
