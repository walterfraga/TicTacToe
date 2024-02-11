from unittest import TestCase

from game.Table import Table


class TestTable(TestCase):
    def test_should_return_no_unoccupied_positions_when_table_is_none(self):
        # Given
        table = Table()
        table.table = None

        # When
        result = table.get_unoccupied_positions()

        # Then
        self.assertEqual([], result)

    def test_should_return_no_unoccupied_positions_when_empty(self):
        # Given
        table = Table()
        table.table = []

        # When
        result = table.get_unoccupied_positions()

        # Then
        self.assertEqual([], result)

    def test_should_return_unoccupied_positions(self):
        # Given
        table = Table()
        table.table = [1, 'X', 3, 'O', 5, 'X', 7, 'O']

        # When
        result = table.get_unoccupied_positions()

        # Then
        self.assertEqual([1, 3, 5, 7], result)

    def test_should_return_has_unoccupied_positions(self):
        # Given
        table = Table()
        table.table = [1, 'X', 3, 'O', 5, 'X', 7, 'O']

        # When
        result = table.has_unoccupied_positions()

        # Then
        self.assertTrue(result)

    def test_should_return_has_no_unoccupied_positions(self):
        # Given
        table = Table()
        table.table = ['X', 'O', 'X', 'O']

        # When
        result = table.has_unoccupied_positions()

        # Then
        self.assertFalse(result)

    def test_should_return_has_no_unoccupied_positions_when_table_empty(self):
        # Given
        table = Table()
        table.table = []

        # When
        result = table.has_unoccupied_positions()

        # Then
        self.assertFalse(result)

    def test_should_return_has_no_unoccupied_positions_when_table_none(self):
        # Given
        table = Table()
        table.table = None

        # When
        result = table.has_unoccupied_positions()

        # Then
        self.assertFalse(result)

    def test_should_return_position_not_occupied(self):
        # Given
        table = Table()
        table.table = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        # When
        result = table.is_position_occupied(0)

        # Then
        self.assertFalse(result)

    def test_should_return_position_is_occupied(self):
        # Given
        table = Table()
        table.table = ['X', 2, 3, 4, 5, 6, 7, 8]

        # When
        result = table.is_position_occupied(0)

        # Then
        self.assertTrue(result)

    def test_should_return_is_first_move(self):
        # Given
        table = Table()
        table.table = [1, 2, 3, 4, 5, 6, 7, 8]

        # When
        result = table.is_first_move()

        # Then
        self.assertTrue(result)

    def test_should_return_is_not_first_move(self):
        # Given
        table = Table()
        table.table = [1, 'X', 3, 4, 5, 6, 7, 8]

        # When
        result = table.is_first_move()

        # Then
        self.assertFalse(result)
