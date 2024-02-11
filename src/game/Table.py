import numbers


class Table:
    def __init__(self):
        self.table = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def print(self):
        print(self.table[0], '|', self.table[1], '|', self.table[2])
        print('---------')
        print(self.table[3], '|', self.table[4], '|', self.table[5])
        print('---------')
        print(self.table[6], '|', self.table[7], '|', self.table[8])
        print('')

    def has_unoccupied_positions(self):
        return self.get_unoccupied_positions().count == 0

    def get_unoccupied_positions(self):
        empty = []
        for position in self.table:
            if str(position).isnumeric():
                empty.append(position)
        return empty

    def is_position_occupied(self, position):
        unoccupied_positions = self.get_unoccupied_positions()
        return position in unoccupied_positions == False

    def is_first_move(self):
        return self.get_unoccupied_positions().count == 9
