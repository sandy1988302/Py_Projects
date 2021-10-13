from random import randint


class Die:

    def __init__(self, side):
        self.side = side

    def rool_die(self):
        return randint(1, self.side)

    def results(self, nums):
        return [self.rool_die() for d in range(nums)]


if __name__ == '__main__':
    a = Die(20)

    print(a.results(6))
