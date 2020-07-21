def latest(scores):
    return scores[-1]
    pass


def personal_best(scores):
    return max(scores)
    pass


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
