def primes(limit):
    answer = list(range(2, limit + 1))
    num = 2
    while num * num < limit:
        if num not in answer:
            num += 1
            continue
        x = 2
        while num * x < limit + num:
            try:
                answer.remove(num * x)
            except:
                pass
            x += 1
        num += 1
    return answer
