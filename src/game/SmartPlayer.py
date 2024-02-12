import random
import time

from game.Player import Player
from game.Table import Table


class SmartPlayer(Player):
    def __init__(self, letter, table):
        super().__init__(letter)
        self.table = table

    def get_move(self):
        print('Computer\'s turn ...')
        time.sleep(1)
        if self.table.is_first_move():
            return random.randint(0, 8)

        remaining_positions = self.table.get_unoccupied_positions()
        copy_table = Table()
        copy_table.table = self.table.table
        for remaining_position in remaining_positions:
            while copy_table.get_winner() in None:
                copy_table.insert(remaining_position, self.letter)
                if copy_table.get_winner() == self.letter:
                    return 10
                elif copy_table.get_winner() is not None:
                    return -1
                else:
                    # call myself
                    pass

