def primes(limit):
    answer = list(range(2, limit + 1))
    for num in range(2, limit + 1):
        x = 2
        if num in answer:
            while num * x < limit + num:
                try:
                    answer.remove(num * x)
                except:
                    pass
                x += 1
    return answer
