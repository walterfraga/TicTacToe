from game.HumanPlayer import HumanPlayer
from game.RandomPlayer import RandomPlayer
from game.Table import Table





class TicTacToe:
    def __init__(self, table):
        self.table = table

    def play(self, player1, player2):
        self.table.print()
        position = None
        current_player = None
        while self.table.has_unoccupied_positions() and self.table.get_winner() is None:
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
            self.table.print()
        winner = self.table.get_winner()
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
