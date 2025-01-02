
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from game_ui import GameUI
from game_config import GameConfig
from game_storage import GameStorage
from src.game_manager import GameManager

def main():
    ui = GameUI()
    config = GameConfig()
    storage = GameStorage()
    game = GameManager(ui, config, storage)
    game.start_game()

if __name__ == "__main__":
    main()
