import random
import time

from game.Player import Player
from game.Table import Table

class Result:
    def __init__(self, position, weight):
        self.position = position
        self.weight = weight

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

        return self.minimax(copy_table, self.letter, 0).position

    def minimax(self, copy_table, letter, depth):
        result = Result(-1, -100)
        for position in copy_table.get_unoccupied_positions():
            weight = 0
            copy_table.insert(position, letter)
            result.position = position
            if copy_table.get_winner() == self.letter:
                weight = 10 - depth
            elif copy_table.get_winner() is not None:
                weight = depth - 10
            else:
                if copy_table.has_unoccupied_positions():
                    new_letter = 'X'
                    if letter == 'X':
                        new_letter = 'O'
                    weight = self.minimax(copy_table, new_letter, depth+1).weight
                else:
                    weight = 0
            if weight > result.weight:
                result.weight = weight
                result.position = position
            copy_table.remove(position)
        return result
