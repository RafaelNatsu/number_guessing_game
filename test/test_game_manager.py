import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.game_manager import GameManager
from src.game_ui import GameUI
from src.game_config import GameConfig
from src.game_storage import GameStorage

class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.ui = GameUI()
        self.config = GameConfig()
        self.storage = GameStorage()
        self.manager = GameManager(self.ui, self.config, self.storage)
        self.manager.difficulty = ('Easy', 10)  # Define o nível de dificuldade

    @patch("random.randint", return_value=42)  # Mocka o número secreto como 42
    @patch("builtins.input", side_effect=["42"])  # Mocka a entrada como "42"
    @patch.object(GameStorage, "save_score")
    def test_run_game_correct_guess(self, mock_save_score, mock_input, mock_random):
        self.manager.run_game()

        # Verifica se o jogo salvou o resultado corretamente como vitória
        mock_save_score.assert_called_once_with('Easy', 1, 42, True)

    @patch("random.randint", return_value=42)  # Mocka o número secreto como 42
    @patch("builtins.input", side_effect=["50", "40", "42"])  # Mocka várias entradas
    @patch.object(GameStorage, "save_score")
    def test_run_game_multiple_attempts(self, mock_save_score, mock_input, mock_random):
        self.manager.run_game()

        # Verifica se o jogo salvou o resultado corretamente após 3 tentativas
        mock_save_score.assert_called_once_with('Easy', 3, 42, True)

    @patch("random.randint", return_value=42)  # Mocka o número secreto como 42
    @patch("builtins.input", side_effect=["50", "60", "70", "80", "90", "100", "101", "102", "103", "104"])  # 10 tentativas erradas
    @patch.object(GameStorage, "save_score")
    def test_run_game_fail(self, mock_save_score, mock_input, mock_random):
        self.manager.run_game()

        # Verifica se o jogo salvou o resultado corretamente como derrota
        mock_save_score.assert_called_once_with('Easy', 10, 42, False)

if __name__ == "__main__":
    unittest.main()
