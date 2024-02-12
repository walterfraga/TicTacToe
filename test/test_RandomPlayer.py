from unittest import TestCase
from unittest.mock import Mock, MagicMock

from game.RandomPlayer import RandomPlayer


class TestRandomPlayer(TestCase):

    def test_should_return_only_available_move(self):
        # Given
        table = Mock()
        table.is_position_occupied = MagicMock(return_value=False)
        player = RandomPlayer('X', table)
        # When
        position = player.get_move()
        # Then
        self.assertIn(position, [0,1,2,3,4,5,6,7,8])
