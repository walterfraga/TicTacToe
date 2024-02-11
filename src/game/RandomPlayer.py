import random
import time

from game.Player import Player


class RandomPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self):
        print('Computer\'s turn ...')
        time.sleep(1)
        return random.randint(0, 8)
