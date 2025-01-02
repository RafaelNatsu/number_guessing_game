import json

class GameStorage:
    @staticmethod
    def save_score(difficulty, attempts, secret_number, won):
        result = {
            "difficulty": difficulty,
            "attempts": attempts,
            "secret_number": secret_number,
            "won": won
        }
        with open('game_scores.txt', 'a') as file:
            file.write(json.dumps(result) + '\n')
