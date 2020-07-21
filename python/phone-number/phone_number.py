import re


class PhoneNumber:
    def __init__(self, number):
        # trash = ['']
        self.number = re.sub('[^0-9]', '', number)
        # print(self.number)
        if len(self.number) == 11 and self.number[0] == '1':
            self.number = self.number[1:]
        if len(self.number) != 10:
            raise ValueError("too many digits")
        if self.number[3] == '1' or self.number[3] == '0':
            raise ValueError("4th digit invalid")
        if self.number[0] == '1' or self.number[0] == '0':
            raise ValueError("1st digit invalid")

        self.area_code = self.number[:3]

    def pretty(self):
        return '(' + self.number[0:3] + ') ' + self.number[3:6] + '-' + self.number[6:]