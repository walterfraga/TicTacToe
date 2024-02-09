import numbers
import random
import time

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_square(self):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_square(self):
        return input(self.letter + '\'s turn. Input move (0-9): ')


class RandomPlayer(Player):
    def __init__(self, letter, table):
        super().__init__(letter)
        self.table = table

    def get_square(self):
        print('Computer\'s trun ...')
        time.sleep(1)
        while True:
            random_number = random.randint(0, 8)
            if isinstance(self.table[random_number], numbers.Number):
                return random_number
