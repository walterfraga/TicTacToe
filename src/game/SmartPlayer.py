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

        copy_table = Table()
        copy_table.table = self.table.table.copy()
        layer = 0
        # position, weight
        return_position = [-1, -10]
        return self.minimax(copy_table, self.letter, layer, return_position)[0]

    def minimax(self, copy_table, letter, layer, return_position):
        for remaining_position in copy_table.get_unoccupied_positions():
            copy_table.insert(remaining_position, letter)
            if copy_table.get_winner() == self.letter:
                weight = 10 - layer
                return_position[1] = weight
                return_position[0] = remaining_position
            elif copy_table.get_winner() is not None:
                weight = layer - 10
                return_position[1] = weight
                return_position[0] = remaining_position
            else:
                if copy_table.has_unoccupied_positions():
                    new_letter = 'X'
                    if letter == new_letter:
                        new_letter = 'O'
                    result = self.minimax(copy_table, new_letter, layer+1, return_position)
                    if result[1] > return_position[1]:
                        return_position[0] = result[0]
                        return_position[1] = result[1]
            copy_table.remove(remaining_position)
        return return_position
