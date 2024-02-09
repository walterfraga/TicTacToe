import numbers

from game.Player import Player


class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.table = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def has_ended(self):
        for square in self.table:
            if isinstance(square, numbers.Number):
                return False
        return True

    def get_player_has_won(self):
        for square in range(3):
            # Check rows [0,1,2] or [3,4,5] or [6,7,8]
            if self.table[square * 3] == self.table[square * 3 + 1] == self.table[square * 3 + 2] != -1:
                return self.table[square * 3]

            # Check columns [0,3,6] or [1,4,7] or [2,5,8]
            if self.table[square] == self.table[square + 3] == self.table[square + 6] != -1:
                return self.table[square]

        # Check diagonals [0,4,8] or [2,4,6]
        if self.table[0] == self.table[4] == self.table[8] != -1:
            return self.table[0]
        if self.table[2] == self.table[4] == self.table[6] != -1:
            return self.table[2]

        return None

    def print_table(self):
        print(self.table[0], '|', self.table[1], '|', self.table[2])
        print('---------')
        print(self.table[3], '|', self.table[4], '|', self.table[5])
        print('---------')
        print(self.table[6], '|', self.table[7], '|', self.table[8])
        print('')

    def play(self):
        self.print_table()
        input_letter = None
        current_player = None
        while not self.has_ended() and self.get_player_has_won() is None:
            if input_letter is None or current_player == self.player2:
                current_player = self.player1
            else:
                current_player = self.player2

            while True:
                input_letter = current_player.get_square()
                if self.is_valid_position(input_letter):
                    break
                else:
                    print(input_letter, ' is an invalid position')

            if isinstance(self.table[int(input_letter)], numbers.Number):
                self.table[int(input_letter)] = current_player.letter
            self.print_table()
        winner = self.get_player_has_won()
        if winner is None:
            print('It is a draw')
        else:
            print('Winner is ', winner)

    def is_valid_position(self, input_letter):
        return (str(input_letter).isnumeric() and int(input_letter) < 9 and
                isinstance(self.table[int(input_letter)], numbers.Number))


if __name__ == '__main__':
    player_1 = Player('X')
    player_2 = Player('O')
    tictactoe = TicTacToe(player_1, player_2)
    tictactoe.play()
