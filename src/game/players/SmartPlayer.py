import random
import time
import math

from game.models.Result import Result
from game.players.Player import Player
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

        return self.minimax(copy_table, self.letter).position

    def minimax(self, copy_table, letter):
        max_player = self.letter
        other_player = 'O' if letter == 'X' else 'X'

        if copy_table.get_winner() == other_player:
            number_unoccupied_positions = len(copy_table.get_unoccupied_positions())
            weight = 1 * (number_unoccupied_positions + 1) if other_player == max_player else -1 * (
                    number_unoccupied_positions + 1)
            return Result(None, weight)
        elif not copy_table.get_unoccupied_positions():
            return Result(None, 0)

        if letter == max_player:
            result = Result(None, -math.inf)
        else:
            result = Result(None, math.inf)

        for possible_move in copy_table.get_unoccupied_positions():
            copy_table.insert(possible_move, letter)
            sim_score = self.minimax(copy_table, other_player)

            copy_table.remove(possible_move)
            sim_score.position = possible_move

            if letter == max_player:
                if sim_score.weight > result.weight:
                    result = sim_score
            else:
                if sim_score.weight < result.weight:
                    result = sim_score
        return result
