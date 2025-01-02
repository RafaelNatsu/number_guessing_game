import random

class GameManager:
    def __init__(self, ui, config, storage):
        self.ui = ui
        self.config = config
        self.storage = storage
        self.secret_number = 0
        self.difficulty = None

    def start_game(self):
        self.ui.show_message("Welcome to the Number Guessing Game!")
        self.ui.show_message("I'm thinking of a number between 1 and 100.")
        self.select_difficulty()
        self.run_game()

    def select_difficulty(self):
        while True:
            try:
                self.ui.show_message("Please select the difficulty level:")
                for i, (name, chances) in enumerate(self.config.LEVELS, start=1):
                    self.ui.show_message(f"{i}. {name} ({chances} chances)")
                choice = int(self.ui.get_input("Enter your choice: "))
                self.difficulty = self.config.get_difficulty(choice)
                self.ui.show_message(f"Selected difficulty: {self.difficulty[0]}\n")
                break
            except (ValueError, IndexError):
                self.ui.show_message("Invalid choice. Please try again.\n")

    def run_game(self):
        self.secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = self.difficulty[1]

        while attempts < max_attempts:
            try:
                guess = int(self.ui.get_input("Enter your guess: "))
                attempts += 1

                if guess == self.secret_number:
                    self.ui.show_message(f"Congratulations! You guessed the number in {attempts} attempts.\n")
                    self.storage.save_score(self.difficulty[0], attempts, self.secret_number, True)
                    return

                direction = "less" if guess > self.secret_number else "greater"
                self.ui.show_message(f"Incorrect! The number is {direction} than {guess}.")
                self.ui.show_message(f"Attempts remaining: {max_attempts - attempts}\n")
            except ValueError:
                self.ui.show_message("Invalid input. Please enter a valid number.\n")

        self.ui.show_message(f"Sorry, you ran out of attempts. The correct number was {self.secret_number}.\n")
        self.storage.save_score(self.difficulty[0], attempts, self.secret_number, False)
