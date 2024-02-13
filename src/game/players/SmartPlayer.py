import math
import random
import time

from game.models.PositionResult import PositionResult
from game.players.Player import Player


class SmartPlayer(Player):
    def __init__(self, letter, table):
        super().__init__(letter)
        self.table = table

    def get_move(self):
        print('Computer\'s turn ...')
        time.sleep(1)
        if self.table.is_first_move():
            return random.randint(0, 8)

        return self.minimax(self.table, self.letter).position

    def minimax(self, param_table, letter):
        max_player = self.letter
        other_player = 'O' if letter == 'X' else 'X'

        if param_table.get_winner() == other_player:
            number_available_positions = len(param_table.get_available_positions())
            weight = 1 * (number_available_positions + 1) if other_player == max_player else -1 * (
                    number_available_positions + 1)
            return PositionResult(None, weight)
        elif not param_table.get_available_positions():
            return PositionResult(None, 0)

        if letter == max_player:
            position_result = PositionResult(None, -math.inf)
        else:
            position_result = PositionResult(None, math.inf)

        for possible_move in param_table.get_available_positions():
            param_table.insert(possible_move, letter)
            simulate_result = self.minimax(param_table, other_player)

            param_table.remove(possible_move)
            simulate_result.position = possible_move

            if letter == max_player:
                if simulate_result.result > position_result.result:
                    position_result = simulate_result
            else:
                if simulate_result.result < position_result.result:
                    position_result = simulate_result
        return position_result
