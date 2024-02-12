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
        layer = 0
        return self.minimax(copy_table, self.letter, layer)

    def minimax(self, copy_table, letter, layer):
        layer += 1
        # position, weight
        return_position = [-1, -100]
        for remaining_position in copy_table.get_unoccupied_positions():
            copy_table.insert(remaining_position, letter)
            if copy_table.get_winner() == self.letter:
                if layer - 10 > return_position[1]:
                    return_position[0] = remaining_position
                    return_position[1] = layer - 10
                    print (letter, ' winner ', str(layer - 10), '. Layer = ', layer)
            elif copy_table.get_winner() is not None:
                if -10 > return_position[1]:
                    return_position[0] = return_position
                    return_position[1] = -10
                    print(letter, ' winner ', str(layer - 10), '. Layer = ', layer)
            else:
                new_letter = 'X'
                if letter == 'X':
                    new_letter = 'O'
                print('no winner call again. Layer = ', layer)
                self.minimax(copy_table, new_letter, layer)
        return return_position[0]
