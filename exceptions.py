class GameError(Exception):
    """Base class for game-related exceptions."""
    pass

class InvalidMoveError(GameError):
    """Exception raised for invalid moves in the game."""
    def __init__(self, message="Invalid move attempted."):
        self.message = message
        super().__init__(self.message)

class GameNotFoundError(GameError):
    """Exception raised when a game is not found."""
    def __init__(self, game_id):
        self.message = f"Game with ID {game_id} not found."
        super().__init__(self.message)

class PlayerNotFoundError(GameError):
    """Exception raised when a player is not found."""
    def __init__(self, player_name):
        self.message = f"Player '{player_name}' not found."
        super().__init__(self.message)

class InvalidInputError(GameError):
    """Exception raised for invalid input provided by the user."""
    def __init__(self, input_value):
        self.message = f"Invalid input: {input_value}. Please check your input and try again."
        super().__init__(self.message)