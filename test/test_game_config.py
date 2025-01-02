import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import unittest
from src.game_config import GameConfig

class TestGameConfig(unittest.TestCase):
    """class for TestGameConfig."""

    def test_get_game_difficulty_valid(self):
        self.assertEqual(GameConfig.get_difficulty(1),('Easy',10))
        self.assertEqual(GameConfig.get_difficulty(2),('Medium',5))
        self.assertEqual(GameConfig.get_difficulty(3),('Hard',1))

    def test_get_difficulty_invalid(self):
        with self.assertRaises(ValueError):
            GameConfig.get_difficulty(0)
        with self.assertRaises(ValueError):
            GameConfig.get_difficulty(4)

if __name__ == "__main__":
    unittest.main()