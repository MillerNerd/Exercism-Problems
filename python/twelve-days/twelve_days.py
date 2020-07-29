from typing import Dict


def recite(start_verse, end_verse):
    days = {1: ("first", "a Partridge in a Pear Tree."),
            2: ("second", "two Turtle Doves, "),
            3: ("third", "three French Hens, "),
            4: ("fourth", "four Calling Birds, "),
            5: ("fifth", "five Gold Rings, "),
            6: ("sixth", "six Geese-a-Laying, "),
            7: ("seventh", "seven Swans-a-Swimming, "),
            8: ("eighth", "eight Maids-a-Milking, "),
            9: ("ninth", "nine Ladies Dancing, "),
            10: ("tenth", "ten Lords-a-Leaping, "),
            11: ("eleventh", "eleven Pipers Piping, "),
            12: ("twelfth", "twelve Drummers Drumming, ")}
    song = []
    for verse in range(start_verse, end_verse + 1):
        song.append("On the %s day of Christmas my true love gave to me: " % days[verse][0])
        for line in range(verse, 0, -1):
            if verse > 1 and line == 1:
                song[-1] = song[-1] + "and " + days[line][1]
            else:
                song[-1] = song[-1] + days[line][1]
    print(song)
    return song
