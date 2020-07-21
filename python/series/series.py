def slices(series, length):
    if length > len(series):
        raise ValueError("Length too long")
    if not series:
        raise ValueError("Series is empty")
    if length < 1:
        raise ValueError("Length too short")
    answer = []
    for i in range(len(series) - length + 1):
        answer.append(series[i:i + length])
    return answer
