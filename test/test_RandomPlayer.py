from unittest import TestCase
from unittest.mock import Mock, MagicMock

from game.players.RandomPlayer import RandomPlayer


class TestRandomPlayer(TestCase):

    def test_should_return_any_available_move(self):
        # Given
        table = Mock()
        table.is_position_available = MagicMock(return_value=True)
        player = RandomPlayer('X', table)
        # When
        position = player.get_move()
        # Then
        self.assertIn(position, [0, 1, 2, 3, 4, 5, 6, 7, 8])
