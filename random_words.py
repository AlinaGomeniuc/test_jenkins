import random

class RandomWords:
    def __init__(self, file):
        self.file = file

    def random(self):
        lines = open(self.file).read().splitlines()
        return random.choice(lines)