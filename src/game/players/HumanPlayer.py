from game.players.Player import Player


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self):
        return input(self.letter + '\'s turn. Input move (0-9): ')
