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
        copy_table.table = self.table.table

        return self.minimax(copy_table, self.letter)

    def minimax(self, copy_table, letter):
        # position, weight
        return_position = [-1,-1]
        for remaining_position in copy_table.get_unoccupied_positions():
            copy_table.insert(remaining_position, letter)
            if copy_table.get_winner() == self.letter:
                if return_position[1] < 10:
                    return_position[0] = return_position
                    return_position[1] = 10
            elif copy_table.get_winner() is not None:
                if return_position[1] < -1:
                    return_position[0] = return_position
                    return_position[1] = -1
            else:
                new_letter = 'X'
                if letter == 'X':
                    new_letter = 'O'
                self.minimax(copy_table, new_letter)
        return return_position
