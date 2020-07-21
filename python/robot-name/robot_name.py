class Robot(object):
    total_names = 100

    def __init__(self):
        # self.name = ''.join(random.choices(string.ascii_uppercase, k=2))
        # self.name += ''.join(random.choices(string.digits, k=4))
        self.name = "AA" + str(Robot.total_names)
        print(self.name)
        Robot.total_names += 1

    def reset(self):
        # self.name = ''.join(random.choices(string.ascii_uppercase, k=2))
        # self.name += ''.join(random.choices(string.digits, k=4))
        self.name = "AA" + str(Robot.total_names)
        print(self.name)
        Robot.total_names += 1
