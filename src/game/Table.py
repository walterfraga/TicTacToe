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
        return len(self.get_unoccupied_positions()) > 0

    def get_unoccupied_positions(self):
        empty = []
        if self.table is not None:
            for position in self.table:
                if str(position).isnumeric():
                    empty.append(position)
        return empty

    def is_position_occupied(self, position):
        unoccupied_positions = self.get_unoccupied_positions()
        if position in unoccupied_positions:
            return False
        return True

    def is_first_move(self):
        size = len(self.table)
        unoccupied_positions = len(self.get_unoccupied_positions())
        return size == unoccupied_positions

    def insert(self, position, value):
        self.table[int(position)] = value

    def remove(self, position):
        self.table[int(position)] = int(position)

    def get_winner(self):
        for position in range(3):
            # Check rows [0,1,2] or [3,4,5] or [6,7,8]
            if self.table[position * 3] == self.table[position * 3] == self.table[position * 3 + 1] == self.table[
                position * 3 + 2] != -1:
                return self.table[position * 3]

            # Check columns [0,3,6] or [1,4,7] or [2,5,8]
            if self.table[position] == self.table[position + 3] == self.table[position + 6] != -1:
                return self.table[position]

        # Check diagonals [0,4,8] or [2,4,6]
        if self.table[0] == self.table[4] == self.table[8] != -1:
            return self.table[0]
        if self.table[2] == self.table[4] == self.table[6] != -1:
            return self.table[2]

        return None
