from typing import Union, Callable, Any

class GameStateValidator:
    """Validator suite for dev-toolkit-91 gaming state verification."""

    def __init__(self, threshold: float = 0.95) -> None:
        self.threshold: float = threshold

    def validate_entity_health(self, value: Union[int, float]) -> bool:
        """Check if entity health resides within sanity bounds for gaming objects."""
        return 0 <= value <= 1000

    def sanitize_input(self, data: Any, transform: Callable[[Any], Any]) -> Any:
        """Functional pipeline application for raw input scrubbing."""
        try:
            return transform(data)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def check_mana_pool(pool: list[int]) -> bool:
        """Logic check for mana distribution integrity."""
        return all(isinstance(m, int) and m >= 0 for m in pool)

    def __call__(self, value: float) -> bool:
        """Direct call access for threshold compliance."""
        return value >= self.threshold