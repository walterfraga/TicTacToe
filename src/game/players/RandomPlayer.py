import random
import time

from game.players.Player import Player


class RandomPlayer(Player):
    def __init__(self, letter, table):
        super().__init__(letter)
        self.table = table

    def get_move(self):
        print('Computer\'s turn ...')
        time.sleep(1)
        while True:
            random_position = random.randint(0, 8)
            if self.table.is_position_available(random_position):
                return random_position
