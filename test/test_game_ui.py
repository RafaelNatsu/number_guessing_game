import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.game_ui import GameUI

class TestGameUi(unittest.TestCase):
    def setUp(self):
        self.test_message = "wdaoç~wdá) 21nck"

    @patch("sys.stdout", new_callable=StringIO)  # Captura o sys.stdout como um objeto StringIO
    def test_show_message(self, mock_stdout):
        # Executa a função
        GameUI.show_message(self.test_message)

        # Verifica se a saída gerada é a esperada
        self.assertEqual(mock_stdout.getvalue(), self.test_message + "\n")

if __name__ == "__main__":
    unittest.main()
