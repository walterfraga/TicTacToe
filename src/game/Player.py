
from game.Table import Table


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        pass







# class SmartPlayer(Player):
#     def __init__(self, letter, table):
#         super().__init__(letter)
#         self.table = table
#
#     def get_move(self):
#         print('Computer\'s turn ...')
#         time.sleep(1)
#         if self.table.is_first_move():
#             while True:
#                 random_position = random.randint(0, 8)
#                 if not self.table.is_position_occupied(random_position):
#                     return random_position
#
#         copy_table = Table()
#         copy_table.table = self.table.table
#
#         return self.minimax(self.letter, copy_table.table)
#
#     def minimax(self, letter, table):
#         current_move_weight = [-1, 0]
#         for remaining_move in table.get_unoccupied_positions():
#             current_move_weight[0] = remaining_move
#             table[remaining_move] = letter
#             winner = get_winner(table)
#             if winner is None:
#                 if letter == 'X':
#                     letter = 'O'
#                 else:
#                     letter = 'X'
#                 new_move_weight = self.minimax(letter, table)
#                 if new_move_weight[1] > current_move_weight[1]:
#                     current_move_weight = new_move_weight
#             else:
#                 if winner == letter:
#                     current_move_weight[1] = 10
#                 else:
#                     current_move_weight[1] = -10
#         return current_move_weight[0]


