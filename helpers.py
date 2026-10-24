import logging
import functools
from typing import Callable, Any

logger = logging.getLogger('dev-toolkit-91')

class GameStateError(Exception):
    """Custom error for corrupted game state."""
    pass

def graceful_recovery(default_val: Any = None) -> Callable:
    """Decorator for suppressing non-critical game logic crashes."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                return func(*args, **kwargs)
            except (ZeroDivisionError, TypeError, ValueError) as e:
                logger.warning(f"Entropy detected in {func.__name__}: {e}. Resetting values.")
                return default_val
            except Exception as e:
                logger.critical(f"Catastrophic engine failure: {e}")
                raise GameStateError(f"State corrupted: {e}") from e
        return wrapper
    return decorator

@graceful_recovery(default_val=0.0)
def calculate_physics_vector(velocity: float, friction: float) -> float:
    """Computes force, safe from division by zero."""
    return velocity / (friction or 0.0001)

def sanitize_input(value: Any) -> str:
    """Sanitize user inputs for game console commands."""
    if not isinstance(value, (str, int, float)):
        return "NULL"
    return str(value).strip()[:255]