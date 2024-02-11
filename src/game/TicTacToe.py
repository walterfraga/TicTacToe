import numbers

from game.Player import HumanPlayer, SmartPlayer, RandomPlayer
from game.Table import Table


class TicTacToe:
    def __init__(self, table):
        self.table = table

    def get_winner(self):
        for square in range(3):
            # Check rows [0,1,2] or [3,4,5] or [6,7,8]
            if self.table.table[square * 3] == self.table.table[square * 3 + 1] == self.table.table[square * 3 + 2] != -1:
                return self.table.table[square * 3]

            # Check columns [0,3,6] or [1,4,7] or [2,5,8]
            if self.table.table[square] == self.table.table[square + 3] == self.table.table[square + 6] != -1:
                return self.table.table[square]

        # Check diagonals [0,4,8] or [2,4,6]
        if self.table.table[0] == self.table.table[4] == self.table.table[8] != -1:
            return self.table.table[0]
        if self.table.table[2] == self.table.table[4] == self.table.table[6] != -1:
            return self.table.table[2]

        return None



    def play(self, player1, player2):
        self.table.print()
        input_letter = None
        current_player = None
        while not self.table.has_unoccupied_positions() and self.get_winner() is None:
            if input_letter is None or current_player == player2:
                current_player = player1
            else:
                current_player = player2

            while True:
                input_letter = current_player.get_square()
                if self.is_valid_position(input_letter):
                    break
                else:
                    print(input_letter, ' is an invalid position')

            if not self.table.is_position_occupied(input_letter):
                self.table.table[int(input_letter)] = current_player.letter
            self.table.print()
        winner = self.get_winner()
        if winner is None:
            print('It is a draw')
        else:
            print('Winner is ', winner)

    def is_valid_position(self, input_letter):
        if str(input_letter).isnumeric():
            position = int(input_letter)
            if position < 9:
                return not self.table.is_position_occupied(position)
        return False


if __name__ == '__main__':
    table = Table()
    tictactoe = TicTacToe(table)
    player_1 = HumanPlayer('X')
    player_2 = RandomPlayer('O', table)
    tictactoe.play(player_1, player_2)
