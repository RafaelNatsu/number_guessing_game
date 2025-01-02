class GameConfig:
    LEVELS = [
        ('Easy', 10),
        ('Medium', 5),
        ('Hard', 1)
    ]

    @staticmethod
    def get_difficulty(choice):
        if 1 <= choice <= len(GameConfig.LEVELS):
            return GameConfig.LEVELS[choice - 1]
        raise ValueError("Invalid difficulty choice.")
