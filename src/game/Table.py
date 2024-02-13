class Table:
    def __init__(self):
        self.table = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def get_printable_table(self):
        print_table = str(self.table[0]) + "|" + str(self.table[1]) + "|" + str(self.table[2])
        print_table += "\n-----\n"
        print_table += str(self.table[3]) + "|" + str(self.table[4]) + "|" + str(self.table[5])
        print_table += "\n-----\n"
        print_table += str(self.table[6]) + "|" + str(self.table[7]) + "|" + str(self.table[8] )
        return print_table

    def has_available_positions(self):
        return len(self.get_available_positions()) > 0

    def get_available_positions(self):
        empty = []
        if self.table is not None:
            for position in self.table:
                if str(position).isnumeric():
                    empty.append(position)
        return empty

    def is_position_available(self, position):
        available_positions = self.get_available_positions()
        if position in available_positions:
            return True
        return False

    def is_first_move(self):
        size = len(self.table)
        available_positions = len(self.get_available_positions())
        return size == available_positions

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
