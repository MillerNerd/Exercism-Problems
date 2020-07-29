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
    song = ["On the %s day of Christmas my true love gave to me: " % days[start_verse][0]]
    # print(song)
    for verse in range(end_verse, start_verse-1, -1):
        song[0] = song[0] + (days[verse][1])
        # print(int(verse))
    print(song)
    return song
    # return ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."]
