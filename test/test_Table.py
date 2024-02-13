from unittest import TestCase

from game.Table import Table


class TestTable(TestCase):
    def test_should_return_no_available_positions_when_table_is_none(self):
        # Given
        table = Table()
        table.table = None

        # When
        result = table.get_available_positions()

        # Then
        self.assertEqual([], result)

    def test_should_return_no_available_positions_when_empty(self):
        # Given
        table = Table()
        table.table = []

        # When
        result = table.get_available_positions()

        # Then
        self.assertEqual([], result)

    def test_should_return_available_positions(self):
        # Given
        table = Table()
        table.table = [0, 'X', 2, 'O', 4, 'X', 5, 'O', 8]

        # When
        result = table.get_available_positions()

        # Then
        self.assertEqual([0, 2, 4, 5, 8], result)

    def test_should_return_has_available_positions(self):
        # Given
        table = Table()
        table.table = [0, 'X', 2, 'O', 4, 'X', 6, 'O', 8]

        # When
        result = table.has_available_positions()

        # Then
        self.assertTrue(result)

    def test_should_return_has_no_available_positions(self):
        # Given
        table = Table()
        table.table = ['X', 'O', 'X', 'O']

        # When
        result = table.has_available_positions()

        # Then
        self.assertFalse(result)

    def test_should_return_has_no_available_positions_when_table_empty(self):
        # Given
        table = Table()
        table.table = []

        # When
        result = table.has_available_positions()

        # Then
        self.assertFalse(result)

    def test_should_return_has_no_available_positions_when_table_none(self):
        # Given
        table = Table()
        table.table = None

        # When
        result = table.has_available_positions()

        # Then
        self.assertFalse(result)

    def test_should_return_position_available(self):
        # Given
        table = Table()
        table.table = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        # When
        result = table.is_position_available(0)

        # Then
        self.assertTrue(result)

    def test_should_return_position_unavailable(self):
        # Given
        table = Table()
        table.table = ['X', 1, 2, 3, 4, 5, 6, 7, 8]

        # When
        result = table.is_position_available(0)

        # Then
        self.assertFalse(result)

    def test_should_return_is_first_move(self):
        # Given
        table = Table()
        table.table = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        # When
        result = table.is_first_move()

        # Then
        self.assertTrue(result)

    def test_should_return_is_not_first_move(self):
        # Given
        table = Table()
        table.table = [0, 'X', 2, 3, 4, 5, 6, 7, 8]

        # When
        result = table.is_first_move()

        # Then
        self.assertFalse(result)

    def test_should_insert_value_in_position(self):
        # Given
        table = Table()
        table.table = [0, 'X', 2, 3, 4, 5, 6, 7, 8]

        # When
        table.insert(3, 'X')

        # Then
        self.assertEqual('X', table.table[3])

    def test_should_remove_value_in_position(self):
        # Given
        table = Table()
        table.table = [0, 'X', 2, 3, 4, 5, 6, 7, 8]

        # When
        table.remove(1)

        # Then
        self.assertEqual(1, table.table[1])

    def test_should_return_no_winner(self):
        # Given
        table = Table()
        table.table = [0, 'X', 2, 3, 4, 5, 6, 7, 8]

        # When
        result = table.get_winner()

        # Then
        self.assertIsNone(result)

    def test_should_row_winner(self):
        # Given
        table = Table()
        table.table = ['O', 'O', 'O', 3, 4, 5, 6, 7, 8]

        # When
        result = table.get_winner()

        # Then
        self.assertEqual('O', result)

    def test_should_return_column_winner(self):
        # Given
        table = Table()
        table.table = ['X', 1, 2, 'X', 4, 5, 'X', 7, 8]

        # When
        result = table.get_winner()

        # Then
        self.assertEqual('X', result)

    def test_should_return_diagonal_1_winner(self):
        # Given
        table = Table()
        table.table = ['O', 1, 2, 3, 'O', 5, 6, 7, 'O']

        # When
        result = table.get_winner()

        # Then
        self.assertEqual('O', result)

    def test_should_return_diagonal_2_winner(self):
        # Given
        table = Table()
        table.table = [0, 1, 'X', 3, 'X', 5, 'X', 7, 8]

        # When
        result = table.get_winner()

        # Then
        self.assertEqual('X', result)

    def test_should_print_table(self):
        # Given
        table = Table()

        # When
        printed_table = table.get_printable_table()

        # Then
        self.assertEqual("0|1|2\n-----\n3|4|5\n-----\n6|7|8", printed_table)

