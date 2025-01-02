import sys
import os
import unittest
from unittest.mock import mock_open, patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.game_storage import GameStorage

class TestGameStorage(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_save_score(self, mock_file):
        GameStorage.save_score("Easy", 3, 10, True)
        mock_file.assert_called_once_with("game_scores.txt", "a")
        mock_file().write.assert_called_once_with(
            '{"difficulty": "Easy", "attempts": 3, "secret_number": 10, "won": true}\n'
        )

if __name__ == "__main__":
    unittest.main()
