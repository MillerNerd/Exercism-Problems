def value(colors):
    resistors = dict(black=0, brown=1, red=2, orange=3, yellow=4, green=5, blue=6, violet=7, grey=8, white=9)
    cnt = ''
    for i in colors:
        cnt += str(resistors[i])
    return int(cnt[:2])
