from game.HumanPlayer import HumanPlayer
from game.RandomPlayer import RandomPlayer
from game.Table import Table


def get_winner(p_table):
    for position in range(3):
        # Check rows [0,1,2] or [3,4,5] or [6,7,8]
        if p_table[position * 3] == p_table[position * 3] == p_table[position * 3 + 1] == p_table[position * 3 + 2] != -1:
            return p_table[position * 3]

        # Check columns [0,3,6] or [1,4,7] or [2,5,8]
        if p_table[position] == p_table[position + 3] == p_table[position + 6] != -1:
            return p_table[position]

    # Check diagonals [0,4,8] or [2,4,6]
    if p_table[0] == p_table[4] == p_table[8] != -1:
        return p_table[0]
    if p_table[2] == p_table[4] == p_table[6] != -1:
        return p_table[2]

    return None


class TicTacToe:
    def __init__(self, table):
        self.table = table

    def play(self, player1, player2):
        self.table.print()
        input_letter = None
        current_player = None
        while self.table.has_unoccupied_positions() and get_winner(self.table.table) is None:
            if input_letter is None or current_player == player2:
                current_player = player1
            else:
                current_player = player2

            while True:
                input_letter = current_player.get_move()
                if self.is_valid_position(input_letter):
                    self.table.table[int(input_letter)] = current_player.letter
                    break
                else:
                    print(input_letter, ' is an invalid position')
            self.table.print()
        winner = get_winner(self.table.table)
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
    player_2 = RandomPlayer('O')
    tictactoe.play(player_1, player_2)
