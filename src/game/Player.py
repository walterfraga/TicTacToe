import numbers
import random
import time


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_square(self):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_square(self):
        return input(self.letter + '\'s turn. Input move (0-9): ')


class RandomPlayer(Player):
    def __init__(self, letter, game):
        super().__init__(letter)
        self.game = game

    def get_square(self):
        print('Computer\'s turn ...')
        time.sleep(1)
        while True:
            random_number = random.randint(0, 8)
            if isinstance(self.game.table[random_number], numbers.Number):
                return random_number


class SmartPlayer(Player):
    def __init__(self, letter, game):
        super().__init__(letter)
        self.game = game

    def get_square(self):
        print('Computer\'s turn ...')
        time.sleep(1)
        if self.game.is_first_move():
            while True:
                random_number = random.randint(0, 8)
                if isinstance(self.game.table[random_number], numbers.Number):
                    return random_number

        remaining_moves = self.game.get_unoccupied_positions()
        return self.minimax(remaining_moves)

    def minimax(self, remaining_moves):
        for remaining_move in remaining_moves:
            self.game.table[remaining_move] = self.letter
            if self.game.get_winning_player() == self.letter:
                self.game.table[remaining_move] = remaining_move
                return remaining_move
            self.game.table[remaining_move] = remaining_move
        return remaining_moves[random.randint(0, len(remaining_moves) - 1)]
