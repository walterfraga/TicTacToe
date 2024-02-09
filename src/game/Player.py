class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_square(self):
        return input(self.letter + '\'s turn. Input move (0-9): ')
