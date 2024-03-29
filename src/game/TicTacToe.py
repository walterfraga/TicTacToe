from game.players.HumanPlayer import HumanPlayer
from game.players.SmartPlayer import SmartPlayer
from game.Table import Table


class TicTacToe:
    def __init__(self, table):
        self.table = table

    def play(self, player1, player2):
        print(self.table.get_printable_table())
        position = None
        current_player = None
        while self.table.has_available_positions() and self.table.get_winner() is None:
            if position is None or current_player == player2:
                current_player = player1
            else:
                current_player = player2

            while True:
                position = current_player.get_move()
                if self.is_valid_position(position):
                    self.table.insert(position, current_player.letter)
                    break
                else:
                    print(position, ' is an invalid position')
            print(self.table.get_printable_table())
        winner = self.table.get_winner()
        if winner is None:
            print('It is a draw')
        else:
            print('Winner is ', winner)

    def is_valid_position(self, input_letter):
        if str(input_letter).isnumeric():
            position = int(input_letter)
            if position < 9:
                return self.table.is_position_available(position)
        return False


if __name__ == '__main__':
    tictactoe_table = Table()
    tictactoe = TicTacToe(tictactoe_table)
    player_1 = HumanPlayer('X')
    player_2 = SmartPlayer('O', tictactoe_table)
    tictactoe.play(player_1, player_2)
