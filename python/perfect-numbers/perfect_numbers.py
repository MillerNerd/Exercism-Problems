def classify(number):
    if number < 1:
        raise ValueError("Number Too Small")
    total = 0
    for i in range(number):
        if i == 0:
            continue
        if number % i == 0:
            total += i
    if number == total:
        return "perfect"
    if number > total:
        return "deficient"
    if number < total:
        return "abundant"
    pass
