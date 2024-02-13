from unittest import TestCase
from unittest.mock import Mock, MagicMock

from game.Table import Table
from game.players.SmartPlayer import SmartPlayer


class TestSmartPlayer(TestCase):
    def test_should_return_random_move_when_first_move(self):
        # Given
        table = Mock()
        table.is_first_move = MagicMock(return_value=True)
        player = SmartPlayer('X', table)
        # When
        position = player.get_move()
        # Then
        self.assertIn(position, [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_should_return_winning_position(self):
        # Given
        table = Table()
        table.table = ['X', 'X', 2, 'O', 'O', 5, 6, 7, 8]
        player = SmartPlayer('X', table)
        # When
        position = player.get_move()
        # Then
        self.assertEqual(2, position)

    def test_should_return_blocking_position(self):
        # Given
        table = Table()
        table.table = ['O', 'O', 2, 'X', 4, 5, 'X', 7, 8]
        player = SmartPlayer('X', table)
        # When
        position = player.get_move()
        # Then
        self.assertEqual(2, position)