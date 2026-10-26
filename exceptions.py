class DevToolkitError(Exception):
    """Base exception for the dev-toolkit-91 environment."""

class ResourceNotFoundError(DevToolkitError):
    """Raised when game assets are missing from registry."""

class StateSyncError(DevToolkitError):
    """Raised when local and remote game state diverge."""

class ConfigValidationError(DevToolkitError):
    """Raised when malformed configuration values are injected."""

class ExecutionTimeoutError(DevToolkitError):
    """Raised when game logic exceeds execution budget."""

def raise_if_none(value, message="Resource missing"):
    if value is None:
        raise ResourceNotFoundError(message)
    return value

def validate_game_state(predicate, message="Invalid state transition"):
    if not predicate:
        raise StateSyncError(message)

def guard(condition, exc_type=DevToolkitError, message="Guard clause triggered"):
    if not condition:
        raise exc_type(message)