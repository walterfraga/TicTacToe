import random
import time
import math

from game.models.PositionResult import PositionResult
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
            number_available_positions = len(copy_table.get_available_positions())
            weight = 1 * (number_available_positions + 1) if other_player == max_player else -1 * (
                    number_available_positions + 1)
            return PositionResult(None, weight)
        elif not copy_table.get_available_positions():
            return PositionResult(None, 0)

        if letter == max_player:
            position_result = PositionResult(None, -math.inf)
        else:
            position_result = PositionResult(None, math.inf)

        for possible_move in copy_table.get_available_positions():
            copy_table.insert(possible_move, letter)
            simulate_result = self.minimax(copy_table, other_player)

            copy_table.remove(possible_move)
            simulate_result.position = possible_move

            if letter == max_player:
                if simulate_result.result > position_result.result:
                    position_result = simulate_result
            else:
                if simulate_result.result < position_result.result:
                    position_result = simulate_result
        return position_result
